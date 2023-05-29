<script>
  import Arte from "$lib/assets/arte.jpg";
  import ciencias from "$lib/assets/ciencias2.jpg";
  import historia from "$lib/assets/historia.jpg";
  import inteligente from "$lib/assets/inteligente.jpg";
</script>

<div class="m-10">
  <div class="w-full bg-pink-400 px-10 rounded-lg items-center py-10 ">
    <div>
      <h1 class="text-3xl font-bold hover:text-pink-200">Fist Step</h1>
      <p class="text-2xl mx-4 mt-3">First chose your favorite categorie..</p>
    </div>
    <div class="grid grid-cols-4 gap-7 my-8 text-center align-middle ">
      <div >
        <h1 class="text-xl font-bold text-center align-middle mb-3 hover:text-pink-200"> Art </h1>
        <button class="rounded-full p-1">
          <img class="rounded-full w-full" src={Arte} alt="perro artista " />
        </button>
      </div>
      <div>
        <h1 class="text-xl font-bold text-center align-middle mb-3 hover:text-pink-200"> Science </h1>
        <button class="rounded-full p-1">
          <img class="rounded-full w-full" src={ciencias} alt="perro de ciencias " />
        </button>
      </div>
      <div>
        <h1 class="text-xl font-bold text-center align-middle mb-3 hover:text-pink-200"> History </h1>
        <button class="rounded-full p-1">
          <img  class="rounded-full w-full text-center justify-center items-center flex-auto" src={historia} alt="perro de historia " />
        </button>
      </div>
      <div>
        <h1 class="text-xl font-bold text-center align-middle mb-3 hover:text-pink-200"> Geography </h1>
        <button class="rounded-full p-1">
          <img  class="rounded-full w-full text-center justify-center items-center" src={inteligente} alt="perro inteligente " />
        </button>
      </div>
    </div>
  </div>
</div>


<style>
    button:active {
 letter-spacing: 3px;
 background-color: hsl(289, 80%, 48%);
 color: hsl(0, 0%, 100%);
 box-shadow: rgb(202, 98, 227) 0px 0px 0px 0px;
 transform: translateY(10px);
 transition: 100ms;

}
</style>