<template>
  <div class="activities">
    <h2 class="activities-title">活动列表</h2>
    <ul class="activities-list">
      <li class="activities-item" v-for="activity in activities" :key="activity.id">
        <div class="activities-item-title">{{ activity.title }}</div>
        <div class="activities-item-date">{{ activity.date }}</div>
        <div class="activities-item-description">{{ activity.description }}</div>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'Activities',
  data() {
    return {
      activities: [
        {
          id: 1,
          title: '第一次活动',
          date: '2022-01-01',
          description: '本次活动内容：...'
        },
        {
          id: 2,
          title: '第二次活动',
          date: '2022-02-01',
          description: '本次活动内容：...'
        },
        {
          id: 3,
          title: '第三次活动',
          date: '2022-03-01',
          description: '本次活动内容：...'
        },
      ]
    }
  }
}
</script>

<style scoped>
.activities {
  padding: 20px;
}

.activities-title {
  font-size: 24px;
  margin-bottom: 10px;
}

.activities-list {
  list-style: none;
  margin: 0;
  padding: 0;
}

.activities-item {
  border: 1px solid #ccc;
  padding: 10px;
  margin-bottom: 10px;
}

.activities-item-title {
  font-size: 18px;
  font-weight: bold;
  margin-bottom: 5px;
}

.activities-item-date {
  font-size: 14px;
  margin-bottom: 5px;
}

.activities-item-description {
  font-size: 14px;
}
</style>
