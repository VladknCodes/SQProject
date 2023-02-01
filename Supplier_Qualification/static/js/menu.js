function addDiv() {
			
			// Меню с разделами сайта. Форма меню с зависимостью от разрешения экрана (версия для PC и мобильная версия).  
			
			var a1 = "Main page";
			var a2 = "Qualification status";
      var a3 = "Audit schedule";
			var a4 = "Qualification process";
			var a5 = "DRA";
			var a6 = "List of QS";


			var outerWidth = window.outerWidth;
			
			if (outerWidth >= 1000) {document.getElementById("inmenu").innerHTML = "<div class='menu'><div class='menu_item'>\
			<a class='m' href='/'>" + a1 +"</a></div><div class='menu_block'></div><div class='menu_item'>\
			<a class='m' href='/qualification_status/'>" + a2 +"</a></div><div class='menu_block'></div><div class='menu_item'>\
      <a class='m' href='/audit_schedule/'>" + a3 +"</a></div><div class='menu_block'></div><div class='menu_item'>\
			<a class='m' href='/qprocess/'>" + a4 +"</a></div><div class='menu_block'></div><div class='menu_item'>\
			<a class='m' href='/dra/'>" + a5 +"</a></div><div class='menu_block'></div><div class='menu_item'>\
			<a class='m' href='/lqs/'>" + a6 +"</a></div></div>";}
			
		
			else {document.getElementById("inmenu").innerHTML = "<div class='menu_mob'><button class='accordion'>Menu site</button><div class='panel'>\
			<p><a class='m' href='/'>" + a1 +"</a></p>\
			<p><a class='m' href='/qualification_status/'>" + a2 +"</a></p>\
      <p><a class='m' href='/audit_schedule/'>" + a3 +"</a></p>\
			<p><a class='m' href='/qprocess/'>" + a4 +"</a></p>\
			<p><a class='m' href='/dra/'>" + a5 +"</a></p>\
			<p><a class='m' href='/lqs/'>" + a6 +"</a></p></div></div>";}
			
			
			var acc = document.getElementsByClassName("accordion");
			var i;

			for (i = 0; i < acc.length; i++) {
				acc[i].addEventListener("click", function() {
					this.classList.toggle("active");
					var panel = this.nextElementSibling;
					if (panel.style.maxHeight){
						panel.style.maxHeight = null;
						}
					 else {
						panel.style.maxHeight = panel.scrollHeight + "px";
					} 
				});
			}
		
			
}
