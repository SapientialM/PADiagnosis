from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Doctor(models.Model):
    """医生表"""
    doctor_id = models.BigAutoField(primary_key=True, verbose_name='医生ID')
    password = models.CharField(max_length=128, verbose_name='密码')
    email = models.EmailField(max_length=100, verbose_name='邮箱')
    full_name = models.CharField(max_length=30, verbose_name='全名')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    last_login = models.DateTimeField(auto_now=True, verbose_name='最后登录时间')
    
    class Meta:
        db_table = 'doctor'
        verbose_name = '医生'
        verbose_name_plural = '医生'
        
    def __str__(self):
        return self.full_name

class Patient(models.Model):
    """患者信息表"""
    patient_id = models.BigAutoField(primary_key=True, verbose_name='患者ID')
    image_style = models.CharField(max_length=30, verbose_name='医学图像类别')
    image = models.ImageField(upload_to='ct_images/%Y/%m/%d/', verbose_name='医学图像')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    created_by = models.ForeignKey('Doctor', on_delete=models.CASCADE, verbose_name='创建人')

    
    class Meta:
        db_table = 'patient'
        verbose_name = '患者'
        verbose_name_plural = '患者'
        
    def __str__(self):
        return f"{self.patient_id} - {self.image_style}"

