// STATUE PANIC! - Input System Eylem Sınıfı
// Normalde Unity Editor'da StatuePanic.inputactions dosyasından otomatik üretilir.
// Bu dosya elle yazılmış eşdeğerdir; .inputactions asset varsa Editor tarafından üzerine yazılabilir.
//
// Kullanım: new StatuePanicInputActions() ile örnek oluştur, Gameplay.Enable() ile aktifleştir.

#if ENABLE_INPUT_SYSTEM
using UnityEngine;
using UnityEngine.InputSystem;

namespace StatuePanic
{
    public class StatuePanicInputActions : IDisposable
    {
        private readonly InputActionMap _gameplay;

        public GameplayActions Gameplay { get; }

        public StatuePanicInputActions()
        {
            _gameplay = new InputActionMap("Gameplay");

            var moveAction = _gameplay.AddAction("Move", InputActionType.Value,
                expectedControlType: "Vector2");
            // WASD
            moveAction.AddCompositeBinding("2DVector")
                .With("Up", "<Keyboard>/w")
                .With("Down", "<Keyboard>/s")
                .With("Left", "<Keyboard>/a")
                .With("Right", "<Keyboard>/d");
            // Gamepad sol stick
            moveAction.AddBinding("<Gamepad>/leftStick");

            var lookAction = _gameplay.AddAction("Look", InputActionType.Value,
                expectedControlType: "Vector2");
            lookAction.AddBinding("<Mouse>/delta")
                      .WithProcessor("ScaleVector2(x=0.1,y=0.1)");
            lookAction.AddBinding("<Gamepad>/rightStick");

            var petrifyAction = _gameplay.AddAction("Petrify", InputActionType.Button);
            petrifyAction.AddBinding("<Keyboard>/space");
            petrifyAction.AddBinding("<Gamepad>/buttonSouth");

            var touchAction = _gameplay.AddAction("Touch", InputActionType.Button);
            touchAction.AddBinding("<Keyboard>/e");
            touchAction.AddBinding("<Gamepad>/buttonWest");

            var tauntAction = _gameplay.AddAction("Taunt", InputActionType.Button);
            tauntAction.AddBinding("<Keyboard>/t");
            tauntAction.AddBinding("<Gamepad>/buttonNorth");

            Gameplay = new GameplayActions(_gameplay);
        }

        public void Dispose() => _gameplay.Dispose();

        public class GameplayActions
        {
            private readonly InputActionMap _map;

            public InputAction Move { get; }
            public InputAction Look { get; }
            public InputAction Petrify { get; }
            public InputAction Touch { get; }
            public InputAction Taunt { get; }

            internal GameplayActions(InputActionMap map)
            {
                _map = map;
                Move = map["Move"];
                Look = map["Look"];
                Petrify = map["Petrify"];
                Touch = map["Touch"];
                Taunt = map["Taunt"];
            }

            public void Enable() => _map.Enable();
            public void Disable() => _map.Disable();
        }
    }
}
#endif
