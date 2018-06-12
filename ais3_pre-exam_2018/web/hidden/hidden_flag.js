var _0x13ed=['getElementById','disp','setInterval','onload','clearInterval','innerHTML','<input\x20type=\x22submit\x22\x20value=\x22Get\x20flag\x20in\x20the\x20next\x20page.\x22/>'];
(function(_0x4ff87b,_0x35e2bc)
	{
	var _0x2c01be=function(_0x216360)
		{
		while(--_0x216360)
			{
			_0x4ff87b['push'](_0x4ff87b['shift']());
		}
	};
	_0x2c01be(++_0x35e2bc);
}
(_0x13ed,0x13f));
var _0x5d44=function(_0x592680,_0x1e9b97)
	{
	_0x592680=_0x592680-0x0;
	var _0x50206c=_0x13ed[_0x592680];
	return _0x50206c;
};
var left=0x0;
var timer=null;
var disp=null;
function countdown()
	{
	left=left-0x1;
	if(timer!=null&&left==0x0)
		{
		window[_0x5d44('0x0')](timer);
		timer=null;
		disp[_0x5d44('0x1')]=_0x5d44('0x2');
	}
	else
		{
		disp[_0x5d44('0x1')]='('+left+')';
	}
}
function setup()
	{
	disp=document[_0x5d44('0x3')](_0x5d44('0x4'));
	left=0xa+parseInt(Math['random']()*0xa);
	timer=window[_0x5d44('0x5')](countdown,0x3e8);
	disp[_0x5d44('0x1')]='('+left+')';
}
window[_0x5d44('0x6')]=setup;
