<template>
    <div>
        <div ref="bodyAnimation" :style="style"></div>
    </div>
</template>
     
<script>
import lottie from "lottie-web";
export default {
    name: "",
    props: {
        options: {
            type: Object,
            required: true,
        },
        width: {
            type: Number,
            default: 200,
        },
        height: {
            type: Number,
            default: 200,
        },
    },
    data() {
        return {
            style: {
                width: this.width ? `${this.width}px` : "100%",
                height: this.height ? `${this.height}px` : "100%",
                overflow: "hidden",
                margin: "0 auto",
            },
        };
    },
    mounted() {
        this.anim = lottie.loadAnimation({
            container: this.$refs.bodyAnimation, // the dom element that will contain the animation
            renderer: "svg",
            loop: this.options.loop !== false,
            autoplay: this.options.autoplay !== false,
            animationData: this.options.animationData,
            rendererSettings: this.options.rendererSettings,
            //   path: sheepJson // the path to the animation json
        });
        this.$emit("animCreated", this.anim);
    },
    methods: {},
};
</script>
     
<style lang="scss" scoped></style>