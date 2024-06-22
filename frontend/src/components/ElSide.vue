<template>
<div id="elside">
  
  <el-menu
    default-active="2"
    class="el-menu-vertical-demo"
    background-color="#303133"
    text-color="white"
    :collapse="isCollapse"
    @open="handleOpen"
    @close="handleClose"
  >
  <el-radio-group v-model="isCollapse" style="margin-bottom: 20px">
    <el-radio-button :value="false">展开</el-radio-button>
    <el-radio-button :value="true">收缩</el-radio-button>
  </el-radio-group>
  <el-menu-item index="5">
    <el-icon><HomeFilled/></el-icon>
    <template #title>
      <router-link :to="{ name: 'Home'}" class="lj">首页</router-link>
  </template>
  </el-menu-item>
    <el-sub-menu index="1">
      <template #title>
        <el-icon><Location/></el-icon>
        <span>功能一</span>
      </template>
      <el-menu-item-group>
        <template #title><span>分组一</span></template>
        <el-menu-item index="1-1">item one</el-menu-item>
        <el-menu-item index="1-2">item two</el-menu-item>
      </el-menu-item-group>
      <el-menu-item-group title="分组二">
        <el-menu-item index="1-3">item three</el-menu-item>
      </el-menu-item-group>
      <el-sub-menu index="1-4">
        <template #title><span>item four</span></template>
        <el-menu-item index="1-4-1">item one</el-menu-item>
      </el-sub-menu>
    </el-sub-menu>
    <el-menu-item index="2">
      <el-icon><icon-menu/></el-icon>
      <template #title>功能2</template>
    </el-menu-item>
    <el-menu-item index="3">
      <el-icon><Document/></el-icon>
      <template #title>
        <router-link :to="{ name: 'ArtiCle'}" class="lj">我的博客</router-link>
    </template>
    </el-menu-item>
    <el-menu-item index="4">
      <el-icon><Setting /></el-icon>
      <template #title>功能三</template>
    </el-menu-item>
  </el-menu>
</div>
</template>

<script setup>
import { ref } from 'vue'
import {
    Location,
	HomeFilled,
    Document,
    Menu as IconMenu,
    Setting,
    } from '@element-plus/icons-vue'

const isCollapse = ref(true)
const handleOpen = (key, keyPath) => {
  console.log(key, keyPath)
}
const handleClose = (key, keyPath) => {
  console.log(key, keyPath)
}
</script>

<style>
.el-menu-vertical-demo{
    height: 100%;
    }
    
.lj{
    color: aliceblue;
}

#elside{
    position: fixed;
    left: 0;
    margin-top:20px;
    width: 10%;
    
    text-align: center;
    font-weight: bold;
    background-color: ##303133;
    
    
}
</style>
