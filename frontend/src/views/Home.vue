<template>

    <BlogHeader/>
    <el-container>
      <el-aside><Cbl/></el-aside>
      <el-main  width="800px"><ArticleList/></el-main>
    </el-container>





    <BlogFooter/>

</template>

<script>
    import BlogHeader from '@/components/BlogHeader.vue'
    import BlogFooter from '@/components/BlogFooter.vue'
    import ArticleList from '@/components/ArticleList.vue'
    import Cbl from '@/components/Cbl.vue'


    export default {
        name: 'Home',
        components: {BlogHeader, BlogFooter, ArticleList,Cbl},
        data: function (){return{}},
    }

</script>