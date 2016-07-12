# Raspberry Pi demo

# 1. Motor 구동하기(i2c)

## 1.1 기본설정

### 1.1.1 i2c-tool 설치

터미널에 다음을 입력

```bash
sudo apt-get install python-smbus
sudo apt-get install i2c-tools
```

### 1.1.2 enable i2c
이용하기에 앞서 RPi에서 i2c 기능을 enable 시켜야한다.
수정하는 방법은 크게 두가지가 있다

#### 1. RPi내 환경설정을 이용해 변경하는 방법
```bash
sudo raspi-config
```
![i2c1](https://cdn-learn.adafruit.com/assets/assets/000/022/831/medium800/learn_raspberry_pi_advancedopt.png?1423001339)
![i2c2](https://cdn-learn.adafruit.com/assets/assets/000/022/832/medium800/learn_raspberry_pi_i2c.png?1423001363)
![i2c3](https://cdn-learn.adafruit.com/assets/assets/000/022/834/medium800/learn_raspberry_pi_wouldyoukindly.png?1423001393)
![i2c4](https://cdn-learn.adafruit.com/assets/assets/000/022/833/medium800/learn_raspberry_pi_i2ckernel.png?1423001374)

그후에 재부팅을 해준다.

```bash
sudo reboot
```

#### 2. 수동으로 i2c 설정하는 방법
RPi 공식 OS인 Raspbian 기준으로 설명하겠다.
/etc/modules 파일을 수정해야 하는데 이 파일은 부팅시에 load할 모듈에 대한 이름을 가지고있다.
이 과정은 아래 링크에서 확인할 수 있다.
> https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c

### 1.1.3 확인하기
장치가 잘 연결 되었는지 확인하기 위해서 아래 명령어를 이용한다.
i2c adderess가 출력이 된다.

```bash
sudo i2cdetect -y 1
```
Raspberry Pi Model B 모델에서는 아래와 같이 0x40와 0x70에 인식된다.
![i2c5](https://cdn-learn.adafruit.com/assets/assets/000/003/055/medium800/learn_raspberry_pi_i2c-detect.png?1396790698)

#### 하지만 우리가 사용할 **RPi 3에서는 0x60 와 0x70**로 인식된다.

## 1.2 라이브러리 설치
라이브러리를 쉽게 이용하기위해 **git**을 설치한다.
현재경로에 **`Adafruit-Motor-HAT-Python-Library`** 폴더가 생성된다.
설치 후 **Adafruit-Motor-HAT-Python-Library** 폴더로 이동한다

```bash
git clone https://github.com/adafruit/Adafruit-Motor-HAT-Python-Library.git
cd Adafruit-Motor-HAT-Python-Library
```

python-dev 설치

```bash 
sudo apt-get install python-dev
```
후에 설치파일을 실행하면 된다.
```bash 
sudo python setup.py install
```

## 1.3 구동하기

지금까지를 간단하게 정리하면

* 현재 모듈은 i2c address 0x60, 0x70으로 인식되어 있다.
* 설치한 라이브러리는 python으로 작성되어있다 
* 

### 1.3.1 DC motor
* DC motor만 사용한다면 4개까지 이용 가능하다
* 한 블럭의 소켓들(블럭당 5개 소켓) 중 가운데 소켓은 사용하지 않는다
* 라이브러리 내에서 각 모터에 대한 addressing은 아래와 같다
![motor1](/img/그림1.png)
위 이미지의 경우 모터에대한 주소가 **3번**이라고 볼 수 있다.

구동에 대한 step-by-step 설명은 아래 링크에서 확인 할 수 있다.

**https://github.com/Jesse-Back/rpi_demo/blob/dev/rpi3/DC_motor_demo.ipynb**

### 1.3.2 stepping motor 
* Stepping motor만 사용한다면 2개까지 이용 가능하다
* 한 블럭의 소켓들(블럭당 5개 소켓) 중 가운데 소켓은 사용하지 않는다
* 라이브러리 내에서 각 모터에 대한 addressing은 아래와 같다

![motor1](/img/그림2.png)

위 이미지의 경우 모터에대한 주소가 **1번**이라고 볼 수 있다.

구동에 대한 step-by-step 설명은 아래 링크에서 확인 할 수 있다.

**https://github.com/Jesse-Back/rpi_demo/blob/dev/rpi3/Step_motor_demo.ipynb**


