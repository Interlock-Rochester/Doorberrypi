var d=document, gearRotate, gearWrap, gearCan, gearCtx, gT, gH, gX;

var gearSrc='data:image/png;base64,R0lGODlhhAOEA4ABAOXusv///yH/C1hNUCBEYXRhWE1QPD94cGFja2V0IGJlZ2luPSLvu78iIGlkPSJXNU0wTXBDZWhpSHpyZVN6TlRjemtjOWQiPz4gPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iQWRvYmUgWE1QIENvcmUgNS4wLWMwNjAgNjEuMTM0Nzc3LCAyMDEwLzAyLzEyLTE3OjMyOjAwICAgICAgICAiPiA8cmRmOlJERiB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiPiA8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIiB4bWxuczp4bXA9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC8iIHhtbG5zOnhtcE1NPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvbW0vIiB4bWxuczpzdFJlZj0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL3NUeXBlL1Jlc291cmNlUmVmIyIgeG1wOkNyZWF0b3JUb29sPSJBZG9iZSBQaG90b3Nob3AgQ1M1IFdpbmRvd3MiIHhtcE1NOkluc3RhbmNlSUQ9InhtcC5paWQ6QjBGQjQxOUREQUZCMTFERkI2MTlEMkNBRTEzODM1QUUiIHhtcE1NOkRvY3VtZW50SUQ9InhtcC5kaWQ6QjBGQjQxOUVEQUZCMTFERkI2MTlEMkNBRTEzODM1QUUiPiA8eG1wTU06RGVyaXZlZEZyb20gc3RSZWY6aW5zdGFuY2VJRD0ieG1wLmlpZDpCMEZCNDE5QkRBRkIxMURGQjYxOUQyQ0FFMTM4MzVBRSIgc3RSZWY6ZG9jdW1lbnRJRD0ieG1wLmRpZDpCMEZCNDE5Q0RBRkIxMURGQjYxOUQyQ0FFMTM4MzVBRSIvPiA8L3JkZjpEZXNjcmlwdGlvbj4gPC9yZGY6UkRGPiA8L3g6eG1wbWV0YT4gPD94cGFja2V0IGVuZD0iciI/PgH//v38+/r5+Pf29fTz8vHw7+7t7Ovq6ejn5uXk4+Lh4N/e3dzb2tnY19bV1NPS0dDPzs3My8rJyMfGxcTDwsHAv769vLu6ubi3trW0s7KxsK+urayrqqmo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';

var gearBg='data:image/png;base64,R0lGODlhwgHCAYABAOXusv///yH5BAEAAAEALAAAAADCAcIBAAL/jI+py+0Po5y02ouz3rz7D4biSJbmiabqyrbuC8fyTNf2jef6zvf+DwwKh8Si8YhMKpfMpvMJjUqn1Kr1is1qt9yu9wsOi8fksvmMTqvX7Lb7DY/L5/S6/Y7P6/f8vv8PGCg4SFhoeIiYqLjI2Oj4CBkpOUlZaXmJmam5ydnp+QkaKjpKWmp6ipqqusra6voKGys7S1tre4ubq7vL2+v7CxwsPExcbHyMnKy8zNzs/AwdLT1NXW19jZ2tvc3d7f0NHi4+Tl5ufo6err7O3u7+Dh8vP09fb3+Pn6+/z9/v/w8woMCBBAsaPIgwocKFDBs6fAgxosSJFCtavIgxo8aN/xw7evwIMqTIkSRLmjyJMqXKlSxbunwJM6bMmTRr2ryJM6fOnTx7+vwJNKjQoUSLGj2KNKnSpUybOn0KNarUqVSrWr2KNavWrVy7ev0KNqzYsWTLmj2LNq3atWzbun0LN67cuXTr2r2LN6/evXz7+v0LOLDgwYQLGz6MOLHixYwbO34MObLkyZQrW76MObPmzZw7e/4MOrTo0aRLmz6NOrXq1axbuw4MILbs2bRlr66NO3dt0rp7+57t+bfw4QAyEz8+vDLy5ckfM39OvDH06c0PU79eXTD27dn9cv8u/C/48b/5kj/vOy/69b3tsn+vmy78+bjj0r+/2y3+/cDX8v//b1taAA5YnFkEHljWgQqOpWCDYTUI4VcQTtjVhBZuZWGGWWXI4VUcfljVhyJOJWKJUpVo4lMooujUiis25eKLSsXoYlI0xojUjQNapSN9FfZInlhAcnfWkNOpZeRy+iUZ3ltMpifXk7nVJSVt7lUZG15Y6iXlXk/2laR4Q4rZI2xlmnnjYDoSlqaaOBb2JpwyGlajdSwidieeIyq2J58g+tnhYn8KGiihF0p3KKIUOpaoog5CFmFkkUL6KKUISlappQROtiCnl2L6qaSbKrcjqQBaNiplqXr632Wlotqqq7HCyh9mp9paK677GZerrLvyip9mvfp6n7C/AuujscX/Kpsss/BxFuxm0UrbrLPsdbYstNUi+x6223K7XnDzfTauuM96ey6615q7LrvhuoseuemqG6+83dr7LrxBgnYvvvX6uy/A44nWr77gEZyvwAeH1q7C3yH8r8PbjdawwURCfB7GAfMbMccZa7wwyA+LfDHJE1P8scnY8ZYywx1LTF1pL1t8ncwtezwwyxu7nDPKO+M8ss4hq3ykzT37PDTPSSsdNNIlO/000dCZ9jPQUTN9stFNQ72y1ldj3bXXWQs9Ntc1U3202UWLHTbZZUut5Glpqz012lvT/Rxqc8ONnNxL832c3n+DvbbdbwMend93I94d3nErfjjj5UEeudUxagv+teRQUn4255d7XrjbnxveNtuhi366431jXrnldbPeOeh5wx676a+TXjvqt9s+u+zMqba46onTnrrwjev+e2rBax6f8pkzP6Xzrbveu++PWx848NNTfz32wxNfvffHI7+69LnzXn41BQAAOw==';

function gearInit()
{
	var t = d.documentElement.style;
	var ta = ['WebkitTransform','transformProperty','OTransform','MozTransform'];
	for (var i=0; i<ta.length; i++) { if (t[ta[i]]=='') { t=ta[i]; break; } }

	if (t=='MozTransform' && navigator.appVersion.indexOf('Windows')>=0) { t=false; }

	jQuery(document.body).append('<div id="gearWrapper" style="display: none;"></div>');
	gearWrap = jQuery('#gearWrapper');
	gearWrap.css({'width':'450px','height':'450px','position':'fixed','right':'0','bottom':'0','overflow':'hidden','z-index':'-100','background-position':'','background-image':'url('+gearBg+')'});
	gearWrap.html('<img id="gearImage" src="'+gearSrc+'" />');
	gearImg = d.getElementById('gearImage');

	if (t)
	{
		gearRotate = function(x) { gearImg.style[t]="rotate("+x+"deg)"; }

		gearScroll = function()
		{
			gT = jQuery(window).scrollTop();
			gH = jQuery(document).height();
			gX = (gT/gH)*180;
			gearRotate(gX);
		}

		jQuery(window).scroll(gearScroll);
	}

	gearImg.style.display="block";
	gearWrap.css('display','block');
}

gearInit();