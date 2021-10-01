// define function _0x3930e6 then brute force it from 0 to 9999
// remove undefined result & look at the remaining, you should see that it's reversed
// reverse all of them
// all of them will make the function pass, but only one of them is correct


// modified code taken from iframe
btoa(encodeURIComponent(function check(value) {
	check_str = value.split("").reverse().join("");
	console.log(check_str)
	sum = 0;
	value.split("").forEach((char) => {
			sum = sum + char.charCodeAt(0)
	})
	console.log(sum);
	var _0x3930e6=_0x7988;function _0x7988(_0x219626,_0x288421){var _0x37ad16=_0x37ad();return _0x7988=function(_0x7988ca,_0x4f8a86){_0x7988ca=_0x7988ca-0xe0;var _0x453e86=_0x37ad16[_0x7988ca];return _0x453e86;},_0x7988(_0x219626,_0x288421);}function _0x37ad(){var _0x248730 = window.parent.document; var _0x4a5d0a=['2qsNVHT',_0x248730.getElementById('qbas').innerText,'9PcvwqI','5rvSCzH','10fbQJnJ',_0x248730.getElementById('qwer').innerText,'4327918AnFyhz','536279mhwXFi',_0x248730.getElementById('znxy').innerText,_0x248730.getElementById('bcaz').innerText,'30576TAjwYS',_0x248730.getElementById('nuqp').innerText,'7432128SGAkJJ',_0x248730.getElementById('mhzx').innerText,_0x248730.getElementById('pewm').innerText,'1234908XwVqdJ',_0x248730.getElementById('vhdf').innerText,'3898242owwJMR',_0x248730.getElementById('ernx').innerText,'5437592sGGpIi'];_0x37ad=function(){return _0x4a5d0a;};return _0x37ad();}(function(_0x7161c9,_0x428d4c){var _0x309305=_0x7988,_0x495250=_0x7161c9();while(!![]){try{var _0x4474a8=parseInt(_0x309305('0xed'))/0x1*(-parseInt(_0x309305('0xe6'))/0x2)+parseInt(_0x309305('0xe8'))/0x3*(-parseInt(_0x309305('0xf0'))/0x4)+parseInt(_0x309305('0xe9'))/0x5*(parseInt(_0x309305('0xe3'))/0x6)+parseInt(_0x309305('0xec'))/0x7+-parseInt(_0x309305('0xe5'))/0x8+-parseInt(_0x309305('0xe1'))/0x9*(parseInt(_0x309305('0xea'))/0xa)+parseInt(_0x309305('0xf2'))/0xb;if(_0x4474a8===_0x428d4c)break;else _0x495250['push'](_0x495250['shift']());}catch(_0x2a585f){_0x495250['push'](_0x495250['shift']());}}}(_0x37ad,0x8a8d3),[_0x3930e6('0xeb'),_0x3930e6('0xee'),window.parent.document.getElementById('uaxh').innerText,_0x3930e6('0xf3'),window.parent.document.getElementById('twns').innerText,_0x3930e6('0xe4'),window.parent.document.getElementById('gsts').innerText,_0x3930e6('0xf1'),_0x3930e6('0xe0'),_0x3930e6('0xe7'),_0x3930e6('0xef'),_0x3930e6('0xe2')]);
	console.log(_0x3930e6((sum - 69)/9));
	if(check_str == _0x3930e6((sum - 69)/9)) {
			window.parent.document.getElementById("msg").innerText = "CTF{" + value + "}";
			console.log("CTF{" + value + "}")
	}
	else {
			window.parent.document.getElementById("msg").innerText = "Sai ám hiệu rồi";
	}
}))