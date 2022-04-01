function importNav() {
    navParent = document.getElementById("navParent");
    nav = document.createElement("div");
    nav.innerHTML = `
<link rel="stylesheet" href="assets/css/main.css">
<div id="top" class="rounded-corners box bar">
    <div class="bar-title">
        <h1>CS-AP-2</h1>
    </div>
    <div class="bar-links">
        <a class="link top-link" href="https://archkitten.github.io/CS-AP-2/">
            <div class="centered-svg-container">
                <div class="centered-svg">
                    <h5 style="margin:10px">Home</h5>
                </div>
            </div>
        </a>
        <a class="link top-link" href="https://archkitten.github.io/CS-AP-2/csa">
            <div class="centered-svg-container">
                <div class="centered-svg">
                    <h5 style="margin:10px">CSA</h5>
                </div>
            </div>
        </a>
        <a class="link bottom-link" href="https://archkitten.github.io/CS-AP-2/csp">
            <div class="centered-svg-container">
                <div class="centered-svg">
                    <h5 style="margin:10px">CSP</h5>
                </div>
            </div>
        </a>
        <a class="link bottom-link" href="https://archkitten.github.io/CS-AP-2/p2" target="_blank" rel="noopener noreferrer" style="margin-right:0 !important;">
            <div class="centered-svg-container">
                <div class="centered-svg">
                    <h5 style="margin:10px">P2</h5>
                </div>
            </div>
        </a>
    </div>
</div>
  `
    navParent.appendChild(nav);
}
