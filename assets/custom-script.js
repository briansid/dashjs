// $("h1").click(function(){
//   $("h1").hide();
// });

// $(document).ready(function(){
//   $("h1").click(function(){
//     $(this).hide();
//   });
// });


// WORKING
// $(document).ready(function(){
//   $(document).on("click", "#table", function(){
//     $(this).hide();
//   });
// });

// $(document).ready( function () {
//     $('#table').DataTable();
// } );


// $(function(){
//     $('#table').DataTable();
// });

// $(document).ready(function(){
// 	$(document).on("click", "tbody tr:first", function(){
// 		$("*").show();
// 	});
// });


// WORKING
$(document).ready(function(){
	$(document).on("click", "tbody tr:eq(1)", function(){
		$("tbody tr:nth-child(1n+3)").slideToggle(1000);
	});
});


// $('tbody tr').eq(0).click(function(){
//     $(this).next().slideToggle(1000);
// });


// alert('If you see this alert, then your custom JavaScript script has run!')