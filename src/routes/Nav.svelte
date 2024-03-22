<script>

    import { Route, Link, linkHandle } from "svelte-micro"
    import About  from './About.svelte'
    import Contactus  from './Contactus.svelte'
    import Hello from './Hello.svelte'


</script>
<style>

</style>



<main class="px-1 py-1.5 md:text-sm lg:text-base">
    <Route>
        <nav use:linkHandle class="bg-blue-300 shadow-lg z-10 px-2 rounded">
            <div class="mx-auto">
                <div class="flex justify-between h-10 px-2">
                    <div class="flex">
                        <!-- Primary Navbar items -->
                        <div class="hidden md:flex items-center space-x-1">
                            <a href="/" class="py-4 px-2 text-gray-800 hover:text-blue-500 font-semibold transition duration-300">Hello</a>
        　　　　             <a href="/about"  class="py-4 px-2 text-gray-800 font-semibold hover:text-blue-500 transition duration-300">About</a>
                            <a href="/contactus"  class="py-4 px-2 text-gray-800 font-semibold hover:text-blue-500 transition duration-300">Contactus</a>
                        </div>
                    </div>

                </div>
            </div>
        </nav>
        <Route path="/" > <Hello/> </Route>
        <Route path="/about"> <About/> </Route>
        <Route path="/contactus"> <Contactus/> </Route>

    </Route>
</main>
