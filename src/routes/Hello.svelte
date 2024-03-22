<script>
    import Counter from '../lib/Counter.svelte'
</script>

<div class="md:bg-cyan-700">


<main class="px-1 flex flex-col h-screen w-full justify-center items-center bg-yellow-100">

    <div class="">
      <spa class="font-light font-sans h-32 w-full items-center text-center text-5xl lg:text-8xl mt-12 text-blue-700">
           Hello World!!
      </spa>

    </div>

   <div class="mt-20">
    <Counter />
   </div>



    <div class="container mx-auto pt-32 px-6 z-10 flex items-center justify-between">
        <div class="container mx-auto px-6 flex flex-col-reverse lg:flex-row justify-between items-center relative">
            <div class="w-full mb-16 md:mb-8 text-center">
                <p>
                  This is powered by Django, Svelte, Vite and Tailwindcss!
                </p>
            </div>
        </div>
    </div>
</main>

</div>