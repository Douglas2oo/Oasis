<template>
    <div class="not-found">
        <h1 class = "text">404 not found</h1>
        <img src = "@/assets/images/404.jpg" alt = "404 not found">
    </div>
</template>


<script setup>

</script>

<style scoped>

.not-found {
    height: 100vh;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;

}

.not-found img {
    height: 80%;
    max-width: max-content;
    max-height: 100%;
}

.text {
    font-size: 5rem;
    font-weight: 700;
    color: #f80606;
    margin-bottom: 2rem;
}

</style>
