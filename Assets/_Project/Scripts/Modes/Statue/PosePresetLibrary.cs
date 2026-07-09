// STATUE PANIC! - Poz preset kütüphanesi (ScriptableObject)
// 20 hazır poz burada tanımlanır. Create > StatuePanic > Pose Preset Library
// İlk 8 poz kodda tanımlı (graybox testi için); kalanı editörde eklenecek.

using UnityEngine;

namespace StatuePanic.Modes.Statue
{
    [CreateAssetMenu(fileName = "PosePresetLibrary", menuName = "StatuePanic/Pose Preset Library")]
    public class PosePresetLibrary : ScriptableObject
    {
        [System.Serializable]
        public class Preset
        {
            public string displayNameTR = "Poz";
            public string displayNameEN = "Pose";
            public Vector3 head, spine, leftArm, rightArm, leftLeg, rightLeg;
        }

        public Preset[] presets = DefaultPresets();

        public PoseData GetPose(byte index)
        {
            if (presets == null || presets.Length == 0 || index >= presets.Length)
                return new PoseData();
            var p = presets[index];
            return new PoseData
            {
                PresetIndex = index,
                HeadEuler = p.head, SpineEuler = p.spine,
                LeftArmEuler = p.leftArm, RightArmEuler = p.rightArm,
                LeftLegEuler = p.leftLeg, RightLegEuler = p.rightLeg
            };
        }

        private static Preset[] DefaultPresets() => new[]
        {
            new Preset { displayNameTR="Düşünen Adam", displayNameEN="The Thinker",
                head=new Vector3(25,0,0), spine=new Vector3(20,0,0),
                rightArm=new Vector3(-110,0,30), leftArm=new Vector3(0,0,10),
                leftLeg=new Vector3(-90,0,0), rightLeg=new Vector3(-90,0,0) },
            new Preset { displayNameTR="Diskobol", displayNameEN="Discobolus",
                spine=new Vector3(0,45,20), rightArm=new Vector3(0,0,-160),
                leftArm=new Vector3(0,0,60), rightLeg=new Vector3(-30,0,0) },
            new Preset { displayNameTR="T-Poz", displayNameEN="T-Pose",
                leftArm=new Vector3(0,0,90), rightArm=new Vector3(0,0,-90) },
            new Preset { displayNameTR="Dab", displayNameEN="Dab",
                head=new Vector3(30,-40,0), rightArm=new Vector3(0,0,-150),
                leftArm=new Vector3(0,0,140), spine=new Vector3(10,-15,0) },
            new Preset { displayNameTR="Selam Dur", displayNameEN="Salute",
                rightArm=new Vector3(-70,0,-45) },
            new Preset { displayNameTR="Kahraman", displayNameEN="Hero",
                spine=new Vector3(-10,0,0), leftArm=new Vector3(0,0,20),
                rightArm=new Vector3(-170,0,0), head=new Vector3(-15,0,0) },
            new Preset { displayNameTR="Tavuk Dansı", displayNameEN="Chicken Dance",
                leftArm=new Vector3(0,0,110), rightArm=new Vector3(0,0,-110),
                leftLeg=new Vector3(-45,30,0), head=new Vector3(0,0,15) },
            new Preset { displayNameTR="Ağlayan Melek", displayNameEN="Weeping Angel",
                head=new Vector3(45,0,0), leftArm=new Vector3(-140,0,-20),
                rightArm=new Vector3(-140,0,20), spine=new Vector3(15,0,0) },
        };
    }
}
