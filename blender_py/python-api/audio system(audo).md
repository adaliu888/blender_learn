# Audio System (aud) 音频系统

## 概述
Audaspace（发音为"outer space"）是一个高级音频库。

## 基本声音播放

此脚本展示了如何使用类：Device、Sound和Handle。

```python
import aud

device = aud.Device()
# 加载声音文件（可以是带音频的视频文件）
sound = aud.Sound('music.ogg')

# 播放音频，这返回一个控制播放/暂停的句柄
handle = device.play(sound)
# 如果音频不太大且会经常使用，可以缓冲它
sound_buffered = aud.Sound.cache(sound)
handle_buffered = device.play(sound_buffered)

# 停止声音（否则它们会播放到结束）
handle.stop()
handle_buffered.stop()
```

## 常量定义

### 音频参数常量
- **aud.AP_LOCATION** - 常量值 3
- **aud.AP_ORIENTATION** - 常量值 4
- **aud.AP_PANNING** - 常量值 1
- **aud.AP_PITCH** - 常量值 2
- **aud.AP_VOLUME** - 常量值 0

### 声道配置常量
- **aud.CHANNELS_INVALID** - 常量值 0
- **aud.CHANNELS_MONO** - 常量值 1
- **aud.CHANNELS_STEREO** - 常量值 2
- **aud.CHANNELS_STEREO_LFE** - 常量值 3
- **aud.CHANNELS_SURROUND4** - 常量值 4
- **aud.CHANNELS_SURROUND5** - 常量值 5
- **aud.CHANNELS_SURROUND51** - 常量值 6
- **aud.CHANNELS_SURROUND61** - 常量值 7
- **aud.CHANNELS_SURROUND71** - 常量值 8

### 编解码器常量
- **aud.CODEC_AAC** - 常量值 1
- **aud.CODEC_AC3** - 常量值 2
- **aud.CODEC_FLAC** - 常量值 3
- **aud.CODEC_INVALID** - 常量值 0
- **aud.CODEC_MP2** - 常量值 4
- **aud.CODEC_MP3** - 常量值 5
- **aud.CODEC_OPUS** - 常量值 8
- **aud.CODEC_PCM** - 常量值 6
- **aud.CODEC_VORBIS** - 常量值 7

### 容器格式常量
- **aud.CONTAINER_AC3** - 常量值 1
- **aud.CONTAINER_FLAC** - 常量值 2
- **aud.CONTAINER_INVALID** - 常量值 0
- **aud.CONTAINER_MATROSKA** - 常量值 3
- **aud.CONTAINER_MP2** - 常量值 4
- **aud.CONTAINER_MP3** - 常量值 5
- **aud.CONTAINER_OGG** - 常量值 6
- **aud.CONTAINER_WAV** - 常量值 7

### 距离模型常量
- **aud.DISTANCE_MODEL_EXPONENT** - 常量值 5
- **aud.DISTANCE_MODEL_EXPONENT_CLAMPED** - 常量值 6
- **aud.DISTANCE_MODEL_INVALID** - 常量值 0
- **aud.DISTANCE_MODEL_INVERSE** - 常量值 1
- **aud.DISTANCE_MODEL_INVERSE_CLAMPED** - 常量值 2
- **aud.DISTANCE_MODEL_LINEAR** - 常量值 3
- **aud.DISTANCE_MODEL_LINEAR_CLAMPED** - 常量值 4

### 格式常量
- **aud.FORMAT_FLOAT32** - 常量值 36
- **aud.FORMAT_FLOAT64** - 常量值 40
- **aud.FORMAT_INVALID** - 常量值 0
- **aud.FORMAT_S16** - 常量值 18
- **aud.FORMAT_S24** - 常量值 19
- **aud.FORMAT_S32** - 常量值 20
- **aud.FORMAT_U8** - 常量值 1

### 采样率常量
- **aud.RATE_11025** - 常量值 11025
- **aud.RATE_16000** - 常量值 16000
- **aud.RATE_192000** - 常量值 192000
- **aud.RATE_22050** - 常量值 22050
- **aud.RATE_32000** - 常量值 32000
- **aud.RATE_44100** - 常量值 44100
- **aud.RATE_48000** - 常量值 48000
- **aud.RATE_8000** - 常量值 8000
- **aud.RATE_88200** - 常量值 88200
- **aud.RATE_96000** - 常量值 96000
- **aud.RATE_INVALID** - 常量值 0

### 状态常量
- **aud.STATUS_INVALID** - 常量值 0
- **aud.STATUS_PAUSED** - 常量值 2
- **aud.STATUS_PLAYING** - 常量值 1
- **aud.STATUS_STOPPED** - 常量值 3

## 核心类

### aud.Device 设备类

Device对象表示音频输出后端，如OpenAL或SDL，但也可能表示文件输出或RAM缓冲区输出。

#### 方法

##### lock()
锁定设备，确保在调用unlock()之前不会从流中读取样本。如果您想同时开始/停止/暂停/恢复一些声音，这很有用。

**注意：**
设备必须解锁与锁定相同的次数才能继续播放。

**警告：**
确保锁定和解锁之间的时间尽可能短，以避免爆音。

##### play(sound, keep=False)
播放声音。

**参数：**
- `sound` (Sound) - 要播放的声音
- `keep` (bool) - 参见Handle.keep

**返回：**
- 可用于控制播放的播放句柄

**返回类型：**
- Handle

##### stopAll()
停止所有正在播放和暂停的声音。

##### unlock()
在lock调用后解锁设备，详情请参见lock()。

#### 属性

- **channels** - 设备的声道数
- **distance_model** - 设备的距离模型
- **doppler_factor** - 设备的多普勒因子
- **format** - 设备的原生采样格式
- **listener_location** - 监听者在3D空间中的位置，3D浮点元组
- **listener_orientation** - 监听者在3D空间中的方向作为四元数，4浮点元组
- **listener_velocity** - 监听者在3D空间中的速度，3D浮点元组
- **rate** - 设备的采样率（Hz）
- **speed_of_sound** - 设备的声音速度。空气中的声音速度通常为343.3 m/s
- **volume** - 设备的总体音量

```python
import aud

# 创建音频设备
device = aud.Device()

# 设置设备属性
device.volume = 0.8
device.listener_location = (0, 0, 0)
device.listener_orientation = (0, 0, 0, 1)

print(f"设备采样率: {device.rate}")
print(f"设备声道数: {device.channels}")
print(f"设备音量: {device.volume}")
```

### aud.DynamicMusic 动态音乐类

DynamicMusic对象允许根据当前场景播放音乐，场景更改由类管理，具有自定义转换的可能性。默认转换是交叉淡入淡出效果，默认场景是静默的，ID为0。

#### 方法

##### addScene(scene)
添加新场景。

**参数：**
- `scene` (Sound) - 场景声音

**返回：**
- 新场景ID

**返回类型：**
- int

##### addTransition(ini, end, transition)
添加新转换。

**参数：**
- `ini` (int) - 转换的初始场景
- `end` (int) - 转换的最终场景
- `transition` (Sound) - 转换声音

**返回：**
- 如果ini或end场景不存在则为false，否则为true

**返回类型：**
- bool

##### pause()
暂停场景播放。

**返回：**
- 操作是否成功

**返回类型：**
- bool

##### resume()
恢复场景播放。

**返回：**
- 操作是否成功

**返回类型：**
- bool

##### stop()
停止场景播放。

**返回：**
- 操作是否成功

**返回类型：**
- bool

#### 属性

- **fadeTime** - 交叉淡入淡出转换的长度（秒）
- **position** - 场景的播放位置（秒）
- **scene** - 当前场景
- **status** - 场景是否正在播放、暂停或停止（=无效）
- **volume** - 场景的音量

```python
import aud

# 创建动态音乐
dynamic_music = aud.DynamicMusic()

# 添加场景
scene1 = aud.Sound.file('scene1.ogg')
scene2 = aud.Sound.file('scene2.ogg')
scene_id1 = dynamic_music.addScene(scene1)
scene_id2 = dynamic_music.addScene(scene2)

# 添加转换
transition = aud.Sound.file('transition.ogg')
dynamic_music.addTransition(scene_id1, scene_id2, transition)

# 控制播放
dynamic_music.volume = 0.7
dynamic_music.fadeTime = 2.0
```

### aud.HRTF 头部相关传递函数类

HRTF对象表示一组头部相关传递函数作为脉冲响应。用于双耳声音。

#### 方法

##### loadLeftHrtfSet(extension, directory)
从目录加载所有HRTF。

**参数：**
- `extension` (string) - hrtf的文件扩展名
- `directory** - HRTF文件所在的路径

**返回：**
- 加载的HRTF对象

**返回类型：**
- HRTF

##### addImpulseResponseFromSound(sound, azimuth, elevation)
向HRTF对象添加新的hrtf。

**参数：**
- `sound` (Sound) - 包含hrtf的声音
- `azimuth` (float) - hrtf的方位角
- `elevation` (float) - hrtf的仰角

**返回：**
- 操作是否成功

**返回类型：**
- bool

```python
import aud

# 加载HRTF
hrtf = aud.HRTF.loadLeftHrtfSet('.wav', '/path/to/hrtf/files')

# 添加脉冲响应
sound = aud.Sound.file('impulse.wav')
hrtf.addImpulseResponseFromSound(sound, 45.0, 30.0)
```

### aud.Handle 句柄类

Handle对象是播放句柄，可用于控制声音的播放。如果声音播放多次，则会有多个句柄。

#### 方法

##### pause()
暂停播放。

**返回：**
- 操作是否成功

**返回类型：**
- bool

##### resume()
恢复播放。

**返回：**
- 操作是否成功

**返回类型：**
- bool

##### stop()
停止播放。

**返回：**
- 操作是否成功

**返回类型：**
- bool

**注意：**
这会使句柄无效。

#### 属性

- **attenuation** - 用于基于距离的源衰减的因子
- **cone_angle_inner** - 源内锥的开角
- **cone_angle_outer** - 源外锥的开角
- **cone_volume_outer** - 源外锥外的音量
- **distance_maximum** - 源的最大距离
- **distance_reference** - 源的参考距离
- **keep** - 声音在到达结束时是否应该保持暂停状态
- **location** - 源在3D空间中的位置，3D浮点元组
- **loop_count** - 声音的（剩余）循环次数
- **orientation** - 源在3D空间中的方向作为四元数，4浮点元组
- **pitch** - 声音的音调
- **position** - 声音的播放位置（秒）
- **relative** - 源的位置、速度和方向是否相对于监听者
- **status** - 声音是否正在播放、暂停或停止（=无效）
- **velocity** - 源在3D空间中的速度，3D浮点元组
- **volume** - 声音的音量
- **volume_maximum** - 源的最大音量
- **volume_minimum** - 源的最小音量

```python
import aud

# 创建设备和声音
device = aud.Device()
sound = aud.Sound.file('music.ogg')

# 播放声音并获取句柄
handle = device.play(sound)

# 控制播放
handle.volume = 0.8
handle.pitch = 1.2
handle.location = (1.0, 0.0, 0.0)

# 暂停和恢复
handle.pause()
handle.resume()

# 停止播放
handle.stop()
```

### aud.ImpulseResponse 脉冲响应类

ImpulseResponse对象表示用于与声音进行卷积的滤波器。

```python
import aud

# 创建脉冲响应
impulse = aud.ImpulseResponse()

# 使用脉冲响应进行卷积
sound = aud.Sound.file('input.wav')
convolved = sound.convolver(impulse)
```

### aud.PlaybackManager 播放管理器类

PlaybackManager对象允许轻松控制按类别组织的音组。

#### 方法

##### addCategory(volume)
添加具有自定义音量的类别。

**参数：**
- `volume` (float) - 新类别的音量

**返回：**
- 新类别的键

**返回类型：**
- int

##### clean()
清理播放管理器中的所有无效和已完成的声音。

##### getVolume(catKey)
检索类别的音量。

**参数：**
- `catKey` (int) - 类别的键

**返回：**
- 类别的音量

**返回类型：**
- float

##### pause(catKey)
暂停类别的播放。

**参数：**
- `catKey` (int) - 类别的键

**返回：**
- 操作是否成功

**返回类型：**
- bool

##### play(sound, catKey)
通过播放管理器播放声音并将其分配给类别。

**参数：**
- `sound` (Sound) - 要播放的声音
- `catKey` (int) - 声音将被添加到的类别的键，如果不存在，将创建一个新类别

**返回：**
- 可用于控制播放的播放句柄

**返回类型：**
- Handle

##### resume(catKey)
恢复类别的播放。

**参数：**
- `catKey` (int) - 类别的键

**返回：**
- 操作是否成功

**返回类型：**
- bool

##### setVolume(volume, catKey)
更改类别的音量。

**参数：**
- `volume` (float) - 新的音量值
- `catKey` (int) - 类别的键

**返回：**
- 操作是否成功

**返回类型：**
- int

##### stop(catKey)
停止类别的播放。

**参数：**
- `catKey` (int) - 类别的键

**返回：**
- 操作是否成功

**返回类型：**
- bool

```python
import aud

# 创建播放管理器
manager = aud.PlaybackManager()

# 添加类别
music_cat = manager.addCategory(0.8)
sfx_cat = manager.addCategory(0.6)

# 播放声音到不同类别
music = aud.Sound.file('music.ogg')
sfx = aud.Sound.file('explosion.wav')

music_handle = manager.play(music, music_cat)
sfx_handle = manager.play(sfx, sfx_cat)

# 控制类别
manager.pause(music_cat)
manager.resume(music_cat)
manager.setVolume(0.5, sfx_cat)
```

### aud.Sequence 序列类

此声音表示序列条目以播放声音序列。

#### 方法

##### add()
向序列添加新条目。

**参数：**
- `sound` (Sound) - 此条目应播放的声音
- `begin` (double) - 开始时间
- `end` (double) - 结束时间或如果由声音确定则为负值
- `skip` (double) - 开头应跳过的秒数

**返回：**
- 添加的条目

**返回类型：**
- SequenceEntry

##### remove()
从序列中移除条目。

**参数：**
- `entry` (SequenceEntry) - 要移除的条目

##### setAnimationData()
向序列写入动画数据。

**参数：**
- `type` (int) - 动画数据的类型
- `frame` (int) - 此数据的帧
- `data` (sequence of float) - 要写入的数据
- `animated` (bool) - 属性是否被动画化

#### 属性

- **channels** - 序列的声道数
- **distance_model** - 序列的距离模型
- **doppler_factor** - 序列的多普勒因子
- **fps** - 监听者在3D空间中的位置，3D浮点元组
- **muted** - 整个序列是否静音
- **rate** - 序列的采样率（Hz）
- **speed_of_sound** - 序列的声音速度

```python
import aud

# 创建序列
sequence = aud.Sequence()

# 添加声音条目
sound1 = aud.Sound.file('sound1.ogg')
sound2 = aud.Sound.file('sound2.ogg')

entry1 = sequence.add(sound1, 0.0, 5.0, 0.0)
entry2 = sequence.add(sound2, 3.0, 8.0, 0.0)

# 设置序列属性
sequence.rate = 48000
sequence.channels = 2
```

### aud.SequenceEntry 序列条目类

SequenceEntry对象表示序列声音的条目。

#### 方法

##### move()
移动条目。

**参数：**
- `begin` (double) - 新的开始时间
- `end` (double) - 新的结束时间或如果未知则为负值
- `skip` (double) - 开头要跳过的秒数

##### setAnimationData()
向序列条目写入动画数据。

**参数：**
- `type` (int) - 动画数据的类型
- `frame` (int) - 此数据的帧
- `data` (sequence of float) - 要写入的数据
- `animated` (bool) - 属性是否被动画化

#### 属性

- **attenuation** - 用于基于距离的源衰减的因子
- **cone_angle_inner** - 源内锥的开角
- **cone_angle_outer** - 源外锥的开角
- **cone_volume_outer** - 源外锥外的音量
- **distance_maximum** - 源的最大距离
- **distance_reference** - 源的参考距离
- **muted** - 条目是否静音
- **relative** - 源的位置、速度和方向是否相对于监听者
- **sound** - 条目表示的声音
- **volume_maximum** - 源的最大音量
- **volume_minimum** - 源的最小音量

```python
import aud

# 创建序列和条目
sequence = aud.Sequence()
sound = aud.Sound.file('sound.ogg')
entry = sequence.add(sound, 0.0, 10.0, 0.0)

# 设置条目属性
entry.volume_maximum = 1.0
entry.volume_minimum = 0.0
entry.location = (1.0, 0.0, 0.0)

# 移动条目
entry.move(2.0, 8.0, 0.5)
```

### aud.Sound 声音类

Sound对象是不可变的，表示可以同时播放多次的声音。它们被称为工厂，因为它们在内部创建用于播放的读取器对象。

#### 类方法

##### buffer(data, rate)
从数据缓冲区创建声音。

**参数：**
- `data` (numpy.ndarray) - 作为二维numpy数组的数据
- `rate` (double) - 采样率

**返回：**
- 创建的Sound对象

**返回类型：**
- Sound

##### file(filename)
创建声音文件的声音对象。

**参数：**
- `filename` (string) - 文件路径

**返回：**
- 创建的Sound对象

**返回类型：**
- Sound

**警告：**
如果文件不存在或无法读取，您不会立即获得异常，但当您尝试开始播放该声音时会获得异常。

##### list()
创建可以包含多个声音的空声音列表。

**参数：**
- `random` (int) - 播放是否随机

**返回：**
- 创建的Sound对象

**返回类型：**
- Sound

##### sawtooth(frequency, rate=48000)
创建播放锯齿波的声音。

**参数：**
- `frequency` (float) - 锯齿波的频率（Hz）
- `rate` (int) - 采样率（Hz）。建议将此值设置为播放设备的采样率以避免重采样

**返回：**
- 创建的Sound对象

**返回类型：**
- Sound

##### silence(rate=48000)
创建播放简单静音的声音。

**参数：**
- `rate` (int) - 采样率（Hz）。建议将此值设置为播放设备的采样率以避免重采样

**返回：**
- 创建的Sound对象

**返回类型：**
- Sound

##### sine(frequency, rate=48000)
创建播放正弦波的声音。

**参数：**
- `frequency` (float) - 正弦波的频率（Hz）
- `rate` (int) - 采样率（Hz）。建议将此值设置为播放设备的采样率以避免重采样

**返回：**
- 创建的Sound对象

**返回类型：**
- Sound

##### square(frequency, rate=48000)
创建播放方波的声音。

**参数：**
- `frequency` (float) - 方波的频率（Hz）
- `rate` (int) - 采样率（Hz）。建议将此值设置为播放设备的采样率以避免重采样

**返回：**
- 创建的Sound对象

**返回类型：**
- Sound

##### triangle(frequency, rate=48000)
创建播放三角波的声音。

**参数：**
- `frequency` (float) - 三角波的频率（Hz）
- `rate` (int) - 采样率（Hz）。建议将此值设置为播放设备的采样率以避免重采样

**返回：**
- 创建的Sound对象

**返回类型：**
- Sound

#### 方法

##### ADSR(attack, decay, sustain, release)
Attack-Decay-Sustain-Release包络声音的音量。注意：目前无法通过此API触发释放。

**参数：**
- `attack` (float) - 攻击时间（秒）
- `decay` (float) - 衰减时间（秒）
- `sustain` (float) - 持续电平
- `release` (float) - 释放电平

**返回：**
- 创建的Sound对象

**返回类型：**
- Sound

##### accumulate(additive=False)
通过累加正输入差异来累积声音，从而生成单调信号。如果可加性设置为true，负输入差异也会被添加，但正输入差异的因子为2。

注意，使用可加性后，信号不再是单调的。

**参数：**
- `additive` - 累积是否应该是可加的

**返回：**
- 创建的Sound对象

**返回类型：**
- Sound

##### addSound(sound)
向声音列表添加新声音。

**参数：**
- `sound` (Sound) - 将添加到列表的声音

**注意：**
您只能向声音列表添加声音。

##### binaural()
使用另一个声音作为源创建双耳声音。原始声音必须是单声道

**参数：**
- `hrtfs` - HRTF集
- `source` (Source) - 表示声音源位置的对象
- `threadPool` (ThreadPool) - 用于并行化卷积的线程池

**返回：**
- 创建的Sound对象

**返回类型：**
- Sound

##### cache()
将声音缓存到RAM中。

如果底层声音从硬盘上的文件读取，这可以节省解码和文件访问所需的CPU使用量，但会消耗大量内存。

**返回：**
- 创建的Sound对象

**返回类型：**
- Sound

**注意：**
只有已知长度的工厂可以被缓冲。

**警告：**
原始PCM数据需要大量空间，只缓冲短工厂。

##### convolver()
创建将对另一个声音应用卷积的声音。

**参数：**
- `impulseResponse` (ImpulseResponse) - 用于卷积声音的滤波器
- `threadPool` (ThreadPool) - 用于并行化卷积的线程池

**返回：**
- 创建的Sound对象

**返回类型：**
- Sound

##### data()
检索声音的数据作为numpy数组。

**返回：**
- 二维numpy浮点数组

**返回类型：**
- numpy.ndarray

**注意：**
缓存声音的最佳效率。

##### delay(time)
通过在另一个声音数据前面添加静音来延迟播放。

**参数：**
- `time` (float) - 在声音前应添加多少秒的静音

**返回：**
- 创建的Sound对象

**返回类型：**
- Sound

##### envelope(attack, release, threshold, arthreshold)
通过在另一个声音数据前面添加静音来延迟播放。

**参数：**
- `attack` (float) - 攻击因子
- `release` (float) - 释放因子
- `threshold` (float) - 一般阈值
- `arthreshold` (float) - 攻击/释放阈值

**返回：**
- 创建的Sound对象

**返回类型：**
- Sound

##### fadein(start, length)
通过在给定时间间隔内线性提高音量来淡入声音。

**参数：**
- `start` (float) - 淡入应开始的秒数
- `length` (float) - 淡入应持续的秒数

**返回：**
- 创建的Sound对象

**返回类型：**
- Sound

**注意：**
在淡入开始前播放静音。

##### fadeout(start, length)
通过在给定时间间隔内线性降低音量来淡出声音。

**参数：**
- `start` (float) - 淡出应开始的秒数
- `length` (float) - 淡出应持续的秒数

**返回：**
- 创建的Sound对象

**返回类型：**
- Sound

**注意：**
淡出后此声音播放静音，因此声音的长度不会改变。

##### filter(b, a=1)
使用提供的IIR滤波器系数过滤声音。没有第二个参数，您将获得FIR滤波器。

如果a序列的第一个值是0，它将自动设置为1。如果a序列的第一个值既不是0也不是1，所有滤波器系数将按此值缩放，使其最终为1，您不必自己缩放。

**参数：**
- `b` (sequence of float) - 分子滤波器系数
- `a` (sequence of float) - 分母滤波器系数

**返回：**
- 创建的Sound对象

**返回类型：**
- Sound

##### highpass(frequency, Q=0.5)
基于传递函数创建二阶高通滤波器。

**参数：**
- `frequency` (float) - 高通的截止频率
- `Q` (float) - 低通的Q因子

**返回：**
- 创建的Sound对象

**返回类型：**
- Sound

##### join(sound)
按顺序播放两个工厂。

**参数：**
- `sound` (Sound) - 第二个播放的声音

**返回：**
- 创建的Sound对象

**返回类型：**
- Sound

**注意：**
两个工厂必须具有相同的规格（声道和采样率）。

##### limit(start, end)
在特定的开始和结束时间内限制声音。

**参数：**
- `start` (float) - 开始时间（秒）
- `end` (float) - 结束时间（秒）

**返回：**
- 创建的Sound对象

**返回类型：**
- Sound

##### loop(count)
循环声音。

**参数：**
- `count` (integer) - 声音应循环的次数。负值表示无限。

**返回：**
- 创建的Sound对象

**返回类型：**
- Sound

**注意：**
这是一个滤波器函数，您可能考虑使用Handle.loop_count代替。

##### lowpass(frequency, Q=0.5)
基于传递函数创建二阶低通滤波器。

**参数：**
- `frequency` (float) - 低通的截止频率
- `Q` (float) - 低通的Q因子

**返回：**
- 创建的Sound对象

**返回类型：**
- Sound

##### mix(sound)
混合两个工厂。

**参数：**
- `sound` (Sound) - 与另一个混合的声音

**返回：**
- 创建的Sound对象

**返回类型：**
- Sound

**注意：**
两个工厂必须具有相同的规格（声道和采样率）。

##### modulate(sound)
调制两个工厂。

**参数：**
- `sound` (Sound) - 与另一个调制的声音

**返回：**
- 创建的Sound对象

**返回类型：**
- Sound

**注意：**
两个工厂必须具有相同的规格（声道和采样率）。

##### mutable()
创建一个在向后搜索时将重新启动的声音。如果原始声音是声音列表，播放的声音可以改变。

**返回：**
- 创建的Sound对象

**返回类型：**
- Sound

##### pingpong()
向前然后向后播放声音。这就像将声音与其反向连接。

**返回：**
- 创建的Sound对象

**返回类型：**
- Sound

##### pitch(factor)
用特定因子改变声音的音调。

**参数：**
- `factor` (float) - 改变音调的因子

**返回：**
- 创建的Sound对象

**返回类型：**
- Sound

**注意：**
这是通过改变底层声音的采样率来完成的，采样率必须是整数，因此因子值被四舍五入，因子可能不是100%准确。

**注意：**
这是一个滤波器函数，您可能考虑使用Handle.pitch代替。

##### rechannel(channels)
重新声道声音。

**参数：**
- `channels` (int) - 新的声道配置

**返回：**
- 创建的Sound对象

**返回类型：**
- Sound

##### resample(rate, high_quality)
重采样声音。

**参数：**
- `rate` (double) - 新的采样率
- `high_quality` (bool) - 当为true时使用更高质量但更慢的重采样器

**返回：**
- 创建的Sound对象

**返回类型：**
- Sound

##### reverse()
反向播放声音。

**返回：**
- 创建的Sound对象

**返回类型：**
- Sound

**注意：**
声音必须具有有限长度且可搜索。建议仅将此用于具有快速准确搜索的工厂，这对于编码音频文件不适用，此类文件应在反向播放前使用cache()进行缓冲。

**警告：**
如果底层声音中的搜索不准确，您可能会听到跳跃/跳跃/爆音。

##### sum()
对声音的样本求和。

**返回：**
- 创建的Sound对象

**返回类型：**
- Sound

##### threshold(threshold=0)
通过将振幅>=阈值的所有样本设置为1，<=-阈值的所有样本设置为-1，之间的所有样本设置为0，从音频波制作阈值波。

**参数：**
- `threshold` (float) - 振幅计数非零的阈值

**返回：**
- 创建的Sound对象

**返回类型：**
- Sound

##### volume(volume)
改变声音的音量。

**参数：**
- `volume` (float) - 新音量

**返回：**
- 创建的Sound对象

**返回类型：**
- Sound

**注意：**
应在[0, 1]范围内以避免削波。

**注意：**
这是一个滤波器函数，您可能考虑使用Handle.volume代替。

##### write(filename, rate, channels, format, container, codec, bitrate, buffersize)
将声音写入文件。

**参数：**
- `filename` (string) - 写入路径
- `rate` (int) - 写入的采样率
- `channels` (int) - 写入的声道数
- `format` (int) - 写入的采样格式
- `container` (int) - 文件的容器格式
- `codec` (int) - 文件中使用的编解码器
- `bitrate` (int) - 写入的比特率
- `buffersize` (int) - 写入缓冲区的大小

#### 属性

- **length** - 声音的采样规格作为具有速率和声道数的元组
- **specs** - 声音的采样规格作为具有速率和声道数的元组

```python
import aud

# 从文件创建声音
sound = aud.Sound.file('music.ogg')

# 从缓冲区创建声音
import numpy as np
data = np.random.random((44100, 2))  # 1秒立体声
sound_from_buffer = aud.Sound.buffer(data, 44100)

# 创建合成声音
sine_wave = aud.Sound.sine(440, 48000)  # 440Hz正弦波
square_wave = aud.Sound.square(220, 48000)  # 220Hz方波
silence = aud.Sound.silence(48000)  # 静音

# 声音处理
filtered = sound.filter([1.0, -0.5], [1.0])  # 低通滤波
delayed = sound.delay(1.0)  # 1秒延迟
faded_in = sound.fadein(0.0, 2.0)  # 2秒淡入
reversed = sound.reverse()  # 反向播放
mixed = sound1.mix(sound2)  # 混合两个声音

# 获取声音信息
print(f"声音长度: {sound.length}")
print(f"声音规格: {sound.specs}")

# 写入文件
sound.write('output.wav', 44100, 2, aud.FORMAT_S16, aud.CONTAINER_WAV, aud.CODEC_PCM, 0, 4096)
```

### aud.Source 源类

源对象表示双耳声音的源位置。

#### 属性

- **azimuth** - 方位角
- **distance** - 距离值。0是最小值，1是最大值
- **elevation** - 仰角

```python
import aud

# 创建源
source = aud.Source()
source.azimuth = 45.0  # 45度方位角
source.elevation = 30.0  # 30度仰角
source.distance = 0.5  # 中等距离

# 用于双耳声音
hrtf = aud.HRTF.loadLeftHrtfSet('.wav', '/path/to/hrtf')
sound = aud.Sound.file('mono.wav')
binaural = sound.binaural(hrtf, source)
```

### aud.ThreadPool 线程池类

ThreadPool用于高效地并行化卷积。

```python
import aud

# 创建线程池
thread_pool = aud.ThreadPool()

# 用于卷积
impulse = aud.ImpulseResponse()
sound = aud.Sound.file('input.wav')
convolved = sound.convolver(impulse, thread_pool)
```

### aud.error 错误类

错误处理类。

```python
import aud

try:
    sound = aud.Sound.file('nonexistent.wav')
except aud.error as e:
    print(f"音频错误: {e}")
```

## 使用示例

### 1. **基本音频播放示例**
```python
import aud

def basic_audio_playback():
    """基本音频播放"""
    
    # 创建音频设备
    device = aud.Device()
    
    # 加载声音文件
    sound = aud.Sound.file('music.ogg')
    
    # 播放声音
    handle = device.play(sound)
    
    # 控制播放
    handle.volume = 0.8
    handle.pitch = 1.0
    
    # 暂停和恢复
    handle.pause()
    handle.resume()
    
    # 停止播放
    handle.stop()
    
    print("基本音频播放完成")

basic_audio_playback()
```

### 2. **声音合成示例**
```python
import aud

def sound_synthesis():
    """声音合成"""
    
    # 创建不同频率的正弦波
    sine_440 = aud.Sound.sine(440, 48000)  # A4音符
    sine_880 = aud.Sound.sine(880, 48000)  # A5音符
    
    # 创建方波和三角波
    square_220 = aud.Sound.square(220, 48000)
    triangle_330 = aud.Sound.triangle(330, 48000)
    
    # 混合声音
    chord = sine_440.mix(sine_880)
    complex_sound = chord.mix(square_220)
    
    # 应用效果
    filtered = complex_sound.lowpass(1000, 0.7)
    delayed = filtered.delay(0.5)
    with_reverb = delayed.mix(filtered.volume(0.3))
    
    # 播放合成声音
    device = aud.Device()
    handle = device.play(with_reverb)
    
    print("声音合成完成")

sound_synthesis()
```

### 3. **3D音频示例**
```python
import aud

def spatial_audio():
    """3D音频"""
    
    # 创建音频设备
    device = aud.Device()
    
    # 设置监听者位置
    device.listener_location = (0, 0, 0)
    device.listener_orientation = (0, 0, 0, 1)
    
    # 加载声音
    sound = aud.Sound.file('explosion.wav')
    
    # 播放声音并设置3D位置
    handle = device.play(sound)
    handle.location = (5, 0, 0)  # 右侧5米
    handle.volume = 1.0
    handle.distance_maximum = 20.0
    handle.distance_reference = 1.0
    
    # 创建移动的声源
    import math
    import time
    
    for i in range(100):
        angle = i * 0.1
        x = 10 * math.cos(angle)
        z = 10 * math.sin(angle)
        handle.location = (x, 0, z)
        time.sleep(0.1)
    
    print("3D音频示例完成")

spatial_audio()
```

### 4. **音频处理示例**
```python
import aud

def audio_processing():
    """音频处理"""
    
    # 加载音频文件
    sound = aud.Sound.file('input.wav')
    
    # 应用各种效果
    # 高通滤波
    highpassed = sound.highpass(500, 0.5)
    
    # 低通滤波
    lowpassed = sound.lowpass(2000, 0.7)
    
    # 音量控制
    quiet = sound.volume(0.3)
    loud = sound.volume(1.5)
    
    # 音调变化
    higher_pitch = sound.pitch(1.5)
    lower_pitch = sound.pitch(0.7)
    
    # 淡入淡出
    faded_in = sound.fadein(0.0, 2.0)
    faded_out = sound.fadeout(sound.length[0] - 2.0, 2.0)
    
    # 反向播放
    reversed = sound.reverse()
    
    # 循环播放
    looped = sound.loop(3)
    
    # 混合多个处理后的声音
    final = highpassed.mix(lowpassed.volume(0.5))
    final = final.mix(faded_in)
    
    # 保存处理后的音频
    final.write('processed.wav', 44100, 2, aud.FORMAT_S16, 
                aud.CONTAINER_WAV, aud.CODEC_PCM, 0, 4096)
    
    print("音频处理完成")

audio_processing()
```

### 5. **播放管理器示例**
```python
import aud

def playback_manager_example():
    """播放管理器示例"""
    
    # 创建播放管理器
    manager = aud.PlaybackManager()
    
    # 添加不同类别
    music_category = manager.addCategory(0.8)
    sfx_category = manager.addCategory(0.6)
    voice_category = manager.addCategory(0.9)
    
    # 加载不同类别的音频
    music = aud.Sound.file('background_music.ogg')
    explosion = aud.Sound.file('explosion.wav')
    voice = aud.Sound.file('voice.wav')
    
    # 播放到不同类别
    music_handle = manager.play(music, music_category)
    sfx_handle = manag