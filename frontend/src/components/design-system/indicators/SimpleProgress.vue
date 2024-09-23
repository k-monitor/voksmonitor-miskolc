<script lang="ts" setup>
import { computed } from 'vue';
export interface SimpleProgressProps {
  id: string;
  colorPrimary: string;
  colorSecondary: string;
  value: number;
  max: number;
  height: string;
}
const props = defineProps<SimpleProgressProps>();
const width = computed(() =>
  props.max !== 0 ? `${(props.value / props.max) * 100}%` : '0%',
);
const color = computed(() =>
  {
    if (props.value < 20)
      return "#C62828"
    if (props.value < 35)
      return "#EF6C00"
    if (props.value < 50)
      return "#F9A825"
    if (props.value < 65)
      return "#9E9D24"
    if (props.value < 80)
      return "#558B2F"
    return "#2E7D32"
  }
);
</script>

<template>
  <div class="wrapper">
    <div class="background">
      <div class="bar"></div>
    </div>
  </div>
</template>
<style lang="scss" scoped>
.wrapper {
  width: 100%;
  height: v-bind('props.height');
  border: 0px;
}
.background {
  background-color: v-bind('props.colorSecondary');
  border-radius: calc(v-bind('props.height') * 0.5);
  width: 100%;
  height: 100%;
}
.bar {
  background-color: v-bind('color');
  border-radius: calc(v-bind('props.height') * 0.5);
  width: v-bind('width');
  height: 100%;
}
</style>
