<template>
    <div class="back">
    <el-tabs v-model="activeName" @tab-click="handleClick" style="margin-left:40px;padding-top:20px">
      <el-tab-pane label="收藏的up主" name="first">
        <!-- 排序 -->
        <KolCardVue></KolCardVue>
      </el-tab-pane>
      <el-tab-pane label="收藏的素材" name="second">
        <NoteCardVue></NoteCardVue>
      </el-tab-pane>
      <el-tab-pane label="收藏的商品" name="third">账号管理</el-tab-pane>
      <el-tab-pane label="收藏的品牌" name="fourth">意见反馈</el-tab-pane>
    </el-tabs>
    </div>
    
</template>
<script>
import KolCardVue from '@/components/Fav/KolCard.vue';
import NoteCardVue from '@/components/Fav/NoteCard.vue';

export default {
  name: 'UserFav',
  data() {
    return {
      activeName: 'first'
    }
  },
  methods: {
    handleClick(tab, event) {
      console.log(tab, event);
    },
  },
  components: {
    KolCardVue,
    NoteCardVue,
  },

}
</script>

<style>

.back{
    background-color: white;
    /* height: 100%; */
}
</style>