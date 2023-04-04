<template>
  <el-form
    ref="ruleFormRef"
    :model="ruleForm"
    :rules="rules"
    label-width="120px"
    class="demo-ruleForm"
    :size="formSize"
    status-icon
  >
    <el-form-item label="报修地点" prop="location">
      <el-input v-model="ruleForm.location" />
    </el-form-item>
    <el-form-item label="问题描述" prop="description">
      <el-input v-model="ruleForm.description" type="textarea" />
    </el-form-item>
    <el-form-item label="报修人员" prop="reporter">
      <el-input v-model="ruleForm.reporter" />
    </el-form-item>
    <el-form-item label="联系方式" prop="contact">
      <el-input v-model="ruleForm.contact" />
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="submitForm(ruleFormRef)">
        提交
      </el-button>
      <el-button @click="resetForm(ruleFormRef)">重置</el-button>
    </el-form-item>
  </el-form>
</template>

<script lang="ts" setup>
import { reactive, ref } from 'vue'
import type { FormInstance, FormRules } from 'element-plus'

const formSize = ref('default')
const ruleFormRef = ref<FormInstance>()
const ruleForm = reactive({
  location: '',
  description: '',
  reporter: '',
  contact: '',
})

const rules = reactive<FormRules>({
  location: [
    { required: true, message: '请输入报修地点', trigger: 'blur' },
  ],
  description: [
    { required: true, message: '请输入问题描述', trigger: 'blur' },
  ],
  reporter: [
    { required: true, message: '请输入报修人员', trigger: 'blur' },
  ],
  contact: [
    { required: true, message: '请输入联系方式', trigger: 'blur' },
  ],
})

const submitForm = async (formEl: FormInstance | undefined) => {
  if (!formEl) return
  await formEl.validate((valid, fields) => {
    if (valid) {
      console.log('submit!')
    } else {
      console.log('error submit!', fields)
    }
  })
}

const resetForm = (formEl: FormInstance | undefined) => {
  if (!formEl) return
  formEl.resetFields()
}
</script>
