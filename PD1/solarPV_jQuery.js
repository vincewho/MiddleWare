$(document).ready(
	function(){
		$("#registration-form").submit(
			function(event){
				//handler -- default action is to submit to the new page
			event.preventDefault();
			}
		);
	}
);