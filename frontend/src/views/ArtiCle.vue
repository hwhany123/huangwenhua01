<template>

    
    <div class="common-layout">
		<el-header><BlogHeader/></el-header>
        
        <el-container>
         
          <el-aside width="200px"><ElSide/></el-aside>
          <el-main><ArticleList/></el-main>
          
        </el-container>
		<el-footer><BlogFooter/></el-footer>
    </div>
    
    

    
    

    

</template>

<script>
    import BlogHeader from '@/components/BlogHeader.vue'
    import BlogFooter from '@/components/BlogFooter.vue'
    import ArticleList from '@/components/ArticleList.vue'
    import ElSide from '@/components/ElSide.vue'


    export default {
        name: 'ArtiCle',
        components: {BlogHeader, BlogFooter, ArticleList,ElSide}
    }
</script>