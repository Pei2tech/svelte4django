<script>
    import { Router, Link, Route } from "svelte5-router";
    import About  from './About.svelte'
    import Contactus  from './Contactus.svelte'
    import Hello from './Hello.svelte'


</script>
<style>

</style>


<main class="px-1 py-1.5 md:text-sm lg:text-base">
     <Router >
        <nav class="bg-blue-300 shadow-lg z-10 px-2 rounded">
            <div class="mx-auto">
                <div class="flex justify-between h-10 px-2">
                    <div class="flex">
                        <!-- Primary Navbar items -->
                        <div class="hidden md:flex items-center space-x-1">
                            <Link to="/" class="py-4 px-2 text-gray-800 hover:text-blue-500 font-semibold transition duration-300">Hello</Link>
                            <Link to="/about"  class="py-4 px-2 text-gray-800 font-semibold hover:text-blue-500 transition duration-300">About</Link>
                            <Link to="/contactus"  class="py-4 px-2 text-gray-800 font-semibold hover:text-blue-500 transition duration-300">Contactus</Link>
                        </div>
                    </div>

                </div>
            </div>
        </nav>

        <Route path="/" component={Hello} />
        <Route path="/about" component={About} />
        <Route path="/contactus" component={Contactus} />
    </Router>
</main>
