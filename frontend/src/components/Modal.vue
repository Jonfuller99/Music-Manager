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
    export default{
        props: ['theme'],
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
        background: white;
        border-radius: 10px;
        display: flex;
        align-items: center;
        flex-direction: column;
        justify-content: center;
    }

    .backdrop{
        top: 0;
        left: 0;
        position: fixed;
        background: rgba(181, 176, 176, 0.5);
        width: 100%;
        height: 100%;
    }
    p {
        color: black;
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