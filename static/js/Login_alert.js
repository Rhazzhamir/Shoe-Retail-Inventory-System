setTimeout(function () {
    const alert = document.querySelector(".alert");
        if (alert) {
            alert.classList.remove("show");
            alert.classList.add("fade");
            setTimeout(() => alert.remove(), 150); 
        }
        }, 3000);
