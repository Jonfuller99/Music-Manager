<template>
    <div class="backdrop" @click.self="closeModal">
        <div class="modal" :class="{sale: theme === 'sale'}">
            <slot></slot>
            <div class="actions">
                <slot name="links"></slot>
            </div>
        </div>
    </div>
</template>

<script>
import AddSongs from './AddSongs.vue';
    export default{
        props: ['theme'],
        components:{AddSongs},
        methods:{
            closeModal(){
                this.$emit('close')
            }
        }
    }

</script>


<style>
    .modal{
        width: 400px;
        padding: 20px;
        margin: 100px auto;
        background: rgb(0, 0, 0);
        border-radius: 10px;
        display: flex;
        align-items: center;
        flex-direction: column;
        justify-content: center;
    }

    p {
        color: white;
    }

    .modal h2 {
        color:rgb(51, 161, 104);
        border: none;
        padding: 0;
        font-weight: 400;
        border-bottom: 1px solid rgb(51, 161, 104);
    }

    .modal.sale{
        background: crimson;
        color: white;
    }
    .modal.sale h2 {
        color: white;
        border-bottom: 1px solid white;

    }
    
    .modal.sale p {
        color: white;
    }

</style>