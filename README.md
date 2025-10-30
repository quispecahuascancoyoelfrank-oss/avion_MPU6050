# 🛩️ Proyecto `avion_mpu6050`

## 📖 Descripción general
Este paquete **ROS 2** se encarga de enlazar **Gazebo Ignition** con **micro-ROS** en un **ESP32** conectado al sensor **MPU6050**, con el objetivo de reflejar los **ángulos de rotación** del sensor en un modelo de avión dentro del entorno de simulación.
 
El sistema permite visualizar en tiempo real la orientación del avión según los datos obtenidos del MPU6050.

---

## ⚙️ Tecnologías utilizadas
- **ROS 2 Humble**
- **Gazebo Ignition**
- **Python 3**
- **CMake**
- **ESP32** (programado con el lenguaje de Arduino)
- **MPU6050**

---

## 🧱 Estructura del proyecto
```bash
.
└── avion_mpu6050
    ├── avion
    │   └── __init__.py
    ├── CMakeLists.txt
    ├── comandos.text
    ├── launch
    │   └── mundo_avion.launch.py
    ├── models
    │   ├── avion.dae
    │   ├── comando_gazebo.text
    │   ├── libSetPoseTopicPlugin.so
    │   └── mundo_avion.sdf
    ├── package.xml
    ├── resource
    │   └── avion
    ├── setup.cfg
    ├── setup.py
    └── test
        ├── test_copyright.py
        ├── test_flake8.py
        └── test_pep257.py
