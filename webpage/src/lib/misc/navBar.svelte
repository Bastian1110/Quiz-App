<script>
  import { slide, fade } from "svelte/transition";
  let logedOut = false;
  const logout = () => {
    localStorage.setItem("token", "");
    localStorage.setItem("username", "");
    logedOut = true;
  };
</script>

<div
  class="navbar bg-gradient-to-r from-indigo-500 via-indigo-500 to-indigo-500 ... roundend-lg px-3 sticky top-0"
>
  <div class="navbar-start">
    <div class="dropdown">
      <label tabindex="0" class="btn btn-ghost btn-circle text-white">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          class="h-5 w-5"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
          ><path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M4 6h16M4 12h16M4 18h7"
          /></svg
        >
      </label>
      <ul
        tabindex="0"
        class="menu menu-compact dropdown-content mt-3 p-2 shadow bg-base-100 rounded-box w-52 bg-indigo-400"
      >
        <li class="text-white font-bold hover:bg-indigo-600">
          <a href="/">Homepage</a>
        </li>
        <li class="text-white font-bold hover:bg-indigo-600">
          <a href="/quiz">Answer Quiz</a>
        </li>
      </ul>
    </div>
  </div>
  <div class="navbar-center">
    <p class=" text-3xl text-white font-bold">QuizzApp</p>
  </div>
  <div class="navbar-end">
    <a href="/login" class="btn mx-2">Login </a>
    <button on:click={logout} class="btn">Logout </button>
  </div>
</div>
{#if logedOut}
  <div
    class="bg-[#72d878] w-[70%] mx-4 p-2 text-white border-4 border-[#303030] fixed bottom-5 right-4"
    transition:fade={{ duration: 200 }}
  >
    <span class="font-bold text-[#000000]">Logout scuccesfull! </span><button
      on:click={() => {
        logedOut = false;
      }}
      class="float-right hover:scale-110"
      ><svg
        class="h-8 w-8 text-black"
        viewBox="0 0 24 24"
        fill="none"
        stroke="currentColor"
        stroke-width="2"
        stroke-linecap="round"
        stroke-linejoin="round"
      >
        <circle cx="12" cy="12" r="10" />
        <line x1="15" y1="9" x2="9" y2="15" />
        <line x1="9" y1="9" x2="15" y2="15" /></svg
      ></button
    >
  </div>
{/if}
