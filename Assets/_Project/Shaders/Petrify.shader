// STATUE PANIC! - Taşlaşma Shader'ı (URP uyumlu, basit ve mobil dostu)
// _PetrifyAmount: 0 = normal renk, 1 = tam taş (gri mermer dokusu)
// _Exposure: görülürken hareket cezası — taştan gerçek renge geri sızma (0-1)
// MaterialPropertyBlock ile PetrifyController tarafından sürülür.

Shader "StatuePanic/Petrify"
{
    Properties
    {
        _BaseMap ("Karakter Dokusu", 2D) = "white" {}
        _BaseColor ("Renk", Color) = (1,1,1,1)
        _StoneMap ("Taş Dokusu", 2D) = "gray" {}
        _StoneTint ("Taş Tonu", Color) = (0.62, 0.62, 0.65, 1)
        _PetrifyAmount ("Taşlaşma", Range(0,1)) = 0
        _Exposure ("Ele Verilme", Range(0,1)) = 0
    }
    SubShader
    {
        Tags { "RenderType"="Opaque" "RenderPipeline"="UniversalPipeline" }
        LOD 100

        Pass
        {
            Name "ForwardLit"
            Tags { "LightMode"="UniversalForward" }

            HLSLPROGRAM
            #pragma vertex vert
            #pragma fragment frag
            #include "Packages/com.unity.render-pipelines.universal/ShaderLibrary/Core.hlsl"
            #include "Packages/com.unity.render-pipelines.universal/ShaderLibrary/Lighting.hlsl"

            struct Attributes { float4 positionOS : POSITION; float3 normalOS : NORMAL; float2 uv : TEXCOORD0; };
            struct Varyings
            {
                float4 positionHCS : SV_POSITION;
                float2 uv : TEXCOORD0;
                float3 normalWS : TEXCOORD1;
                float3 positionWS : TEXCOORD2;
            };

            TEXTURE2D(_BaseMap);  SAMPLER(sampler_BaseMap);
            TEXTURE2D(_StoneMap); SAMPLER(sampler_StoneMap);

            CBUFFER_START(UnityPerMaterial)
                float4 _BaseMap_ST;
                float4 _StoneMap_ST;
                half4 _BaseColor;
                half4 _StoneTint;
                half _PetrifyAmount;
                half _Exposure;
            CBUFFER_END

            Varyings vert(Attributes IN)
            {
                Varyings OUT;
                OUT.positionHCS = TransformObjectToHClip(IN.positionOS.xyz);
                OUT.positionWS = TransformObjectToWorld(IN.positionOS.xyz);
                OUT.normalWS = TransformObjectToWorldNormal(IN.normalOS);
                OUT.uv = TRANSFORM_TEX(IN.uv, _BaseMap);
                return OUT;
            }

            half4 frag(Varyings IN) : SV_Target
            {
                half4 baseCol = SAMPLE_TEXTURE2D(_BaseMap, sampler_BaseMap, IN.uv) * _BaseColor;
                half4 stoneCol = SAMPLE_TEXTURE2D(_StoneMap, sampler_StoneMap, IN.uv * 2.0) * _StoneTint;

                // Taşlaşma karışımı; exposure taşı geri deler (aşağıdan yukarı sızma efekti)
                half exposeBleed = _Exposure * saturate(1.2 - frac(IN.positionWS.y * 0.35));
                half blend = saturate(_PetrifyAmount - exposeBleed);
                half4 albedo = lerp(baseCol, stoneCol, blend);

                // Basit Lambert (mobil dostu; Faz 2'de Lit'e yükseltilebilir)
                Light mainLight = GetMainLight();
                half ndotl = saturate(dot(normalize(IN.normalWS), mainLight.direction));
                half3 lighting = mainLight.color * (ndotl * 0.75 + 0.25);

                return half4(albedo.rgb * lighting, 1);
            }
            ENDHLSL
        }
    }
    FallBack "Universal Render Pipeline/Simple Lit"
}
