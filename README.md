## MCGPU Lite v1.5环境配置

参考此链接信息，已比较详细
<https://github.com/SEU-CT-Recon/MCGPULite_v1.5?tab=readme-ov-file>
***

## 文件准备
输入的模体文件<链接>

**说明**
模体文件的尺寸为附加物体尺寸加n (*n为pmma板厚度，并在文件名中标明*) ，附加物的材料ID对应、密度和厚度信息如下
```
# 定义附加物厚度
thickness_iodine_2 = 2
thickness_iodine_5 = 5
thickness_fe = 1
thickness_ta = 1
thickness_pt = 1
thickness_ba = 50
thickness_bone = 40
thickness_co2_2 = 2
thickness_co2_5 = 5
# 定义材料密度
density_air = 0.00120479  # 空气
density_pmma = 1.18  # PMMA
density_iodine = 0.35  # 碘块 (350 mg/mL)
density_fe = 7.874  # 铁
density_ta = 16.65  # 钽
density_pt = 21.45  # 铂
density_ba = 2  # 钡
density_bone = 1.92  # 骨骼
density_co2 = 0.001977  # CO₂
# 定义材料 ID
AirID = 1
PMMAID = 2
IodineID = 3
FeID = 4 # (用钢代替)
TaID = 5 # （用w代替 73->74）
PtID = 6 # (用钨替代 78->74)
BaID = 7 # （用碘化铯代替 csl）
BoneID = 8 
CO2ID = 9 # （用空气）
```
完整模体文件创建代码参见此
<https://github.com/hzseu71/wandong_2/blob/main/miniMutiVoxCreate.py>
模体文件由此代码于本地创建

---
## MCGPU Litev1.5运行配置文件参数详情
文件参见此处，注意此文件不可直接运行，通过下面的脚本进行执行（或替换掉.in文件内的所有 **{}** 占位符后可以执行）
测试能谱文件
<https://github.com/hzseu71/wandong_2/tree/main/spec>
材料文件
<https://github.com/hzseu71/wandong_2/tree/main/material>
注意修改这几处路径
```
# 输入能谱路径
/mnt/no2/huzhen/spec/{spectrum}.txt    # X-RAY ENERGY SPECTRUM FILE
# 输出文件路径
/mnt/no2/huzhen/file_mc/100kv_C01_mm_422_2/P{thickness}PLM_MM_100kv_{fileRemarks}_repeat_{run}                # OUTPUT IMAGE FILE NAME
# 输入模体文件路径
/mnt/no2/huzhen/vox/miniMM/miniMM_2/P{thickness}mm_MutipleMaterialsBot_mini_with1m.vox    # VOXEL GEOMETRY FILE (penEasy 2008 format; .gz accepted)
# 输入材料路径
#[SECTION MATERIAL FILE LIST v.2020-03-03]   
/mnt/no2/huzhen/material/air__5-120keV.mcgpu.gz                   #  1st MATERIAL FILE (.gz accepted)
/mnt/no2/huzhen/material/PMMA__5-120keV.mcgpu.gz                 #  2nd MATERIAL FILE
/mnt/no2/huzhen/material/blood90_iodine10__5-120keV.mcgpu.gz
/mnt/no2/huzhen/material/steel__5-120keV.mcgpu.gz
/mnt/no2/huzhen/material/W__5-120keV.mcgpu.gz
/mnt/no2/huzhen/material/W__5-120keV.mcgpu.gz
/mnt/no2/huzhen/material/W__5-120keV.mcgpu.gz
/mnt/no2/huzhen/material/bone_ICRP110__5-120keV.mcgpu.gz
/mnt/no2/huzhen/material/air__5-120keV.mcgpu.gz 
```
---
## 批量执行脚本(通过运行此py脚本以进行mcgpu程序执行)
文件参见于此<https://github.com/hzseu71/wandong_2/blob/main/miniMutiVoxCreate.py>
```
"""
通过此代码调用.in的配置文件进行mcgpu运行,以方便批量运行
"""
spectrum_list = ['spectrum100_Copper0.1mm'] # 输入能谱文件列表
thickness_list = range(400, 401, 50) # 模拟厚度范围
repeat_count = 1 # 单张重复次数
histories_per_run = 7e9 # 单次模拟的光子数
base_seed = 2342 # 随机数种子
file_remarks = 'mini_422_bone' # 文件名尾巴
```



