function ajaxInject( target, elementid )
{
	var xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function()
	{
		if (this.readyState == 4 && this.status == 200)
		/* The state of the xhttp request can be one of the following:
		 *	0   UNSENT  open() has not been called yet.
		 *	1   OPENED  send() has been called.
		 *	2   HEADERS_RECEIVED    send() has been called, and headers and status are available.
		 *	3   LOADING Downloading; responseText holds partial data.
		 *	4   DONE    The operation is complete.
		 *
		 *	the 200 status signifies an OK response to the request
		 */
		{
			document.getElementById( elementid ).innerHTML = this.responseText;
		}
	};
	xhttp.open('GET', target, true);
	xhttp.send();
}
