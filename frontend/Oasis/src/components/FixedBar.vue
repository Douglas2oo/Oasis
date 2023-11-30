<!-- components/FixedBar.vue -->
<template>
    <div class="fixed-bar">
        <textarea v-model="articleText" placeholder="Write your new article here..." :maxlength="200"></textarea>
        <button @click="publishArticle">Publish</button>
    </div>
</template>

<script setup>
import { ref, reactive } from 'vue'
import axios from 'axios'
import { useRouter } from "vue-router"

const router = useRouter();
const Userdata = reactive({
    id: router.currentRoute.value.query.id,
})

// The input text of the article
const articleText = ref('');

// Button function
const publishArticle = async () => {

    // set up request data
    let data = {
        content: articleText.value, // Use the content in the text box
        author: Userdata.id, // Use the ID of the current user
    };

    try {
        const response = await axios.post('http://127.0.0.1:8000/article/', data, { withCredentials: true })

        // Send a request to the backend
        console.log(response);
    } catch (error) {
        console.error(error);
        console.log('error');
    }
    window.location.reload()
};

</script>

<style scoped>
/* Fixed bar at the bottom for new article */
.fixed-bar {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    background-color: #4CAF50;
    padding: 0px;
    display: flex;
    justify-content: space-between;
    color: white;
    z-index: 3;
}

/* Larger textarea */
.fixed-bar textarea {
    width: 110%;
    height: 60px;
    border-radius: 8px;
    padding: 5px;
    resize: none;
    font-size: 18px;
}

/* Larger placeholder text */
.fixed-bar textarea::placeholder {
    font-size: 18px;
    color: #aaa;
}

/* Publish button styling */
.fixed-bar button {
    background-color: #4CAF50;
    border: none;
    color: white;
    padding: 15px 32px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 26px;
    font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
    margin: 4px 2px;
    cursor: pointer;
    border-radius: 8px;
}
</style>
