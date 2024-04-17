# TUMBA

[![TUMBA logo](/DOCS/logo.png)](https://github.com/ploschka/python-tumba)

## Сборка

1. Клонируйте репозиторий и перейдите в созданную директорию

    ```sh
    git clone --recurse-submodules https://github.com/ploschka/python-tumba.git
    cd python-tumba
    ```

2. Сконфигурируйте проект с помощью `cmake`

    ```sh
    cmake -S . -B build
    ```

    Сборка настраивается следующими дополнительными флагами

    |Флаг|Значения|Значение по умолчанию|Описание|
    |----|--------|---------------------|--------|
    |-DCMAKE_BUILD_TYPE=$VALUE|Debug; Release; RelWithDebInfo; MinSizeRel|Debug|Определяет тип сборки. Для детальной информации смотреть [CMAKE_BUILD_TYPE](https://llvm.org/docs/CMake.html#cmake-build-type)|

3. Соберите проект

    ```sh
    cmake --build build
    ```

4. Скопируйте из директории build файл pycom-api.*.so в директорию python-tumba

## Зависимости

- LLVM 17.0.6

## Системные требования

- Архитектура x86 / x86-64
