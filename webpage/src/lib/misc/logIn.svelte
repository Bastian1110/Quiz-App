<script lang="js">
  import { slide, fade } from "svelte/transition";

  let register = true;
  let setRegister = () => {
    register = !register;
  };

  let username;
  let password;

  let signUpError = false;
  let signUpSuccess = false;
  let signInError = false;
  let signInSuccess = false;

  async function signUp() {
    try {
      const response = await fetch("http://137.184.20.150:8080/user/register", {
        method: "POST",
        headers: { "content-type": "application/x-www-form-urlencoded" },
        body: new URLSearchParams({ username, password }),
      });
      let data = await response.json();
      console.log(data);
      if (data.result === 1) {
        signUpError = true;
        console.log("miaaau");
      } else {
        signUpSuccess = true;
      }
      username = "";
      password = "";
    } catch (err) {
      signUpError = 1;
      username = "";
      password = "";
    }
  }

  let lusername = "";
  let lpassword = "";
  async function signIn() {
    console.log({ lusername, lpassword });
    try {
      const response = await fetch("http://137.184.20.150:8080/user/login", {
        method: "POST",
        headers: { "content-type": "application/x-www-form-urlencoded" },
        body: new URLSearchParams({ username: lusername, password: lpassword }),
      });
      let data = await response.json();
      if (data.result === 1) {
        signInError = true;
      } else {
        signInSuccess = true;
        localStorage.setItem("token", data.token);
        localStorage.setItem("username", lusername);
      }
      lusername = "";
      lpassword = "";
    } catch (err) {
      console.log(err);
      signInError = true;
      lusername = "";
      lpassword = "";
    }
  }
</script>

<div class="m-10 bg-gradient-to-r from-purple-300 to-pink-300 py-10 rounded-lg">
  {#if register}
    <div
      class="transition-all m-6 ml-10 mt-[28vh] w-[45%] text-purple-800"
      transition:slide={{ duration: 1000 }}
    >
      <h1 class="m-4 pb-4 text-6xl text-purple-800">Welcome!</h1>
      <form>
        <input
          bind:value={lusername}
          type="username"
          class="bg-white block m-4 border-4 border-purple-900 w-[70%] p-2 text-xl placeholder:text-[#c0c0c0] placeholder:text-xl placeholder:text-right placeholder:pr-4"
          placeholder="tu usuario ..."
        />
        <input
          bind:value={lpassword}
          type="password"
          class="bg-white block m-4 border-4 border-purple-900 w-[70%] p-2 text-xl placeholder:text-[#c0c0c0] placeholder:text-xl placeholder:text-right placeholder:pr-4"
          placeholder="contraseña ..."
        />
        <button
          on:click={signIn}
          class="transition duration-200 block m-4 border-4 border-purple-800 text-purple-800 w-[25%] p-2 text-xl hover:scale-105 hover:bg-[#8db3f5]"
          >LogIn</button
        >
        <span class="ml-4 mt-2"
          >Dont have an account? <button
            class="font-bold hover:scale-105"
            on:click={setRegister}>Register</button
          ></span
        >
      </form>
    </div>
    {#if signInError}
      <div
        class="bg-[#ed4545] float-right w-[70%] mx-4 p-2 text-white border-4 border-[#303030]"
        transition:fade={{ duration: 200 }}
      >
        <span class="font-bold text-[#000000]">Oh no! Error. </span><button
          on:click={() => {
            signInError = false;
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
    {#if signInSuccess}
      <div
        class="bg-[#91ff99] float-right w-[70%] mx-4 p-2 text-white border-4 border-[#303030]"
        transition:fade={{ duration: 200 }}
      >
        <span class="font-bold text-[#000000]">Login scuccesfull! </span><button
          on:click={() => {
            signInSuccess = false;
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
  {/if}

  {#if !register}
    <div
      class="m-6 ml-10 mt-[18vh] w-[45%] float-right"
      transition:slide={{ duration: 1000 }}
    >
      <h1 class="float-right m-4 pb-4 text-6xl">Register</h1>
      <form on:submit|preventDefault>
        <input
          bind:value={username}
          type="text"
          class="float-right block mx-4 mb-3 border-4 border-primary w-[70%] p-2 text-xl text-right placeholder:text-[#c0c0c0] placeholder:text-xl placeholder:text-right placeholder:pr-4"
          placeholder="username ..."
        />
        <input
          bind:value={password}
          type="password"
          class="float-right block mx-4 mb-3 border-4 border-primary w-[70%] p-2 text-xl text-right placeholder:text-[#c0c0c0] placeholder:text-xl placeholder:text-right placeholder:pr-4"
          placeholder="password ..."
        />
        <input
          type="password"
          class="float-right block mx-4 mb-3 border-4 border-primary w-[70%] p-2 text-xl text-right placeholder:text-[#c0c0c0] placeholder:text-xl placeholder:text-right placeholder:pr-4"
          placeholder="password again ..."
        />
        <button
          on:click={signUp}
          class="float-right transition duration-200 block mx-4 mb-3 border-4 border-black w-[25%] p-2 text-xl hover:scale-105 hover:text-white hover:bg-primary"
          >Register</button
        >
        <span class="float-right block mr-10 mt-2"
          >Already have an account? <button
            class="font-bold hover:scale-105"
            on:click={setRegister}>LogIn</button
          ></span
        >
      </form>
      {#if signUpSuccess}
        <div
          class="bg-[#91ff99] float-right w-[70%] mx-4 p-2 text-white border-4 border-[#303030]"
          transition:fade={{ duration: 200 }}
        >
          <span class="font-bold text-[#000000]">User created! </span><button
            on:click={() => {
              signUpSuccess = false;
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
      {#if signUpError}
        <div
          class="bg-[#ed4545] float-right w-[70%] mx-4 p-2 text-white border-4 border-[#303030]"
          transition:fade={{ duration: 200 }}
        >
          <span class="font-bold text-[#000000]">Error! </span><button
            on:click={() => {
              signUpError = false;
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
    </div>
  {/if}
</div>
