<template>
  <el-form ref="ruleFormRef" :model="ruleForm" :rules="rules" label-width="120px" class="demo-ruleForm" :size="formSize"
    status-icon>
    <el-form-item label="报告厅申请" prop="Location">
      <el-select v-model="ruleForm.Location" placeholder="请选择报告厅">
        <el-option label="东区报告厅" value="东区报告厅" />
        <el-option label="西区报告厅" value="西区报告厅" />
      </el-select>
    </el-form-item>

    <el-form-item label="申请人员" prop="Reporter">
      <el-input v-model="ruleForm.Reporter" />
    </el-form-item>
    <el-form-item label="联系方式" prop="Phonenum">
      <el-input v-model="ruleForm.Phonenum" />
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
import { ElMessage } from 'element-plus';
import apiClient from "../apiClient";
import { reactive, ref, defineEmits } from 'vue';
import type { FormInstance, FormRules } from 'element-plus';

// Vue3自定义事件，.ts写法。当表单成功提交后，这个事件将被触发，使其他组件能够监听
interface Emits {
  (event: 'form-submitted'): void;
}
const emit = defineEmits<Emits>();

const formSize = ref('default');
const ruleFormRef = ref<FormInstance>();
const ruleForm = reactive({
  Location: '',
  Description: '开报告厅，调字幕',
  Reporter: '',
  Phonenum: '',
});

const rules = reactive<FormRules>({
  Location: [
    { required: true, message: '请输入报修地点', trigger: 'blur' },
  ],
  Description: [
    { required: true, message: '请输入问题描述', trigger: 'blur' },
  ],
  Reporter: [
    { required: true, message: '请输入报修人员', trigger: 'blur' },
  ],
  Phonenum: [
    { required: true, message: '请输入联系方式', trigger: 'blur' },
  ],
});

const submitForm = async (formEl: FormInstance | undefined) => {
  if (!formEl) return;
  await formEl.validate(async (valid, fields) => {
    if (valid) {
      try {
        const response = await apiClient.post('/api/repairs', ruleForm);
        console.log('Form submitted successfully:', response);
        ElMessage({
          message: '表单提交成功！',
          type: 'success',
        });
        emit('form-submitted');
      } catch (error) {
        console.error('Error submitting form:', error);
        ElMessage({
          message: '表单提交失败，请稍后重试。',
          type: 'error',
        });
      }
    } else {
      console.log('error submit!', fields);
      ElMessage({
        message: '表单验证失败，请检查输入内容。',
        type: 'warning',
      });
    }
  });
};

const resetForm = (formEl: FormInstance | undefined) => {
  if (!formEl) return;
  formEl.resetFields();
};
</script>


