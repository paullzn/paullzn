package
{
	import com.vanceinfo.meathill.Tag;
	
	import flash.display.*;
	import flash.events.*;
	import flash.net.*;
	import flash.text.*;
	import flash.ui.*;
	
	import flashx.textLayout.formats.BackgroundColor;
    
    public class TagCloud extends flash.display.Sprite
    {
        public function TagCloud()
        {
            super();
         
            this.stage.scaleMode = StageScaleMode.NO_SCALE;
            this.stage.align = StageAlign.TOP_LEFT;
			
			//Inteface to javascript BEGIN
            tcolor = this.loaderInfo.parameters.tcolor != null ? Number(this.loaderInfo.parameters.tcolor) : 3355443;
            tcolor2 = this.loaderInfo.parameters.tcolor2 != null ? Number(this.loaderInfo.parameters.tcolor2) : 10048768;
            hicolor = this.loaderInfo.parameters.hicolor != null ? Number(this.loaderInfo.parameters.hicolor) : 0;
            tspeed = this.loaderInfo.parameters.tspeed != null ? Number(this.loaderInfo.parameters.tspeed) / 100 : 1;
            distr = this.loaderInfo.parameters.distr != null ? false : true;
            if (loaderInfo.parameters["data"])
            {
                myXML = XML(loaderInfo.parameters["data"]);
            }
            else 
            {
                myXML = new XML("<billboard><item url='http://skiyo.cn' query='Skiyo' trend='0' intro='' url1=''/>" +
					"<item url='http://skiyo.cn' query='百度搜索' trend='0' intro='' url1=''/>"+
					"<item url='http://skiyo.cn' query='谷歌搜索' trend='0' intro='' url1=''/>"+
					"<item url='http://skiyo.cn' query='新浪网' trend='0' intro='' url1=''/>"+
					"<item url='http://skiyo.cn' query='腾讯网' trend='0' intro='' url1=''/>"+
					"<item url='http://skiyo.cn' query='搜狐网' trend='0' intro='' url1=''/>"+
					"<item url='http://skiyo.cn' query='凤凰网' trend='0' intro='' url1=''/>"+
					"<item url='http://skiyo.cn' query='新华网' trend='0' intro='' url1=''/>"+
					"<item url='http://skiyo.cn' query='中央电视台网' trend='0' intro='' url1=''/>"+
					"<item url='http://skiyo.cn' query='人民网' trend='0' intro='' url1=''/>"+
					"<item url='http://skiyo.cn' query='人人网' trend='0' intro='' url1=''/>"+
					"<item url='http://skiyo.cn' query='开心网' trend='0' intro='' url1=''/>"+
					"<item url='http://skiyo.cn' query='优酷网' trend='0' intro='' url1=''/>"+
					"<item url='http://skiyo.cn' query='太平洋电脑网' trend='0' intro='' url1=''/>"+
					"<item url='http://skiyo.cn' query='中华英才网' trend='0' intro='' url1=''/>"+
					"<item url='http://skiyo.cn' query='携程旅行网' trend='0' intro='' url1=''/>"+
					"<item url='http://skiyo.cn' query='淘宝网' trend='0' intro='' url1=''/>"+
					"<item url='http://skiyo.cn' query='当当网' trend='0' intro='' url1=''/>"+
					"<item url='http://skiyo.cn' query='58同城网' trend='0' intro='' url1=''/>"+
					"</billboard>");
            }
			//Interface to javascript END
			
			_setBackground();
            init(myXML);
            return;
        }
		
		//initialize the background graph
		private function _setBackground():void{
			[Embed(source='assets/background.jpg')]
			var BackgroundClass:Class;
			_image = new BackgroundClass(); 
			
			_image.width = radius;
			_image.height = radius;
			addChild(_image);
		}
		
		//set the component order by depth
        private function depthSort():void
        {
            var loc1:*=NaN;
            var loc2:*=NaN;
            _tagList.sortOn("cz", Array.DESCENDING | Array.NUMERIC);
            loc1 = 0;
            loc2 = 0;
            while (loc2 < _tagList.length) 
            {
                holder.setChildIndex(_tagList[loc2], loc2);
                if (_tagList[loc2].active)
                {
                    loc1 = loc2;
                }
                loc2 = (loc2 + 1);
            }
			
            holder.setChildIndex(_tagList[loc1], (_tagList.length - 1));
            return;
        }

        private function sineCosine(arg1:Number, arg2:Number, arg3:Number):void
        {
            sa = Math.sin(arg1 * _sensitive);
            ca = Math.cos(arg1 * _sensitive);
            sb = Math.sin(arg2 * _sensitive);
            cb = Math.cos(arg2 * _sensitive);
            sc = Math.sin(arg3 * _sensitive);
            cc = Math.cos(arg3 * _sensitive);
            return;
        }

        private function xmlLoaded(arg1:flash.events.Event):void
        {
            myXML = XML(myLoader.data);
            init(myXML);
            return;
        }

        private function init(inputData:XML):void
        {
            var node:XML = null;
            var newTag:Tag = null;
            radius = 100;
			
			//initialize the sensitive, the biger the more sensitive
            _sensitive = Math.PI / 90;
            d = 200;
            sineCosine(0, 0, 0);
            _tagList = [];
            _active = false;
            lasta = 1;
            lastb = 1;
            holder = new MovieClip();
            addChild(holder);
            resizeHolder();
            
            for each (node in inputData.item)
            {
                newTag = new Tag( node, 0x333333, 0xef3809);
                holder.addChild(newTag);
                _tagList.push(newTag);
            }
			
            positionAll();
            addEventListener(Event.ENTER_FRAME, updateTags);
            stage.addEventListener(Event.MOUSE_LEAVE, mouseExitHandler);
            stage.addEventListener(MouseEvent.MOUSE_MOVE, mouseMoveHandler);
            stage.addEventListener(Event.RESIZE, resizeHandler);
            return;
        }

        private function getNumberFromString(arg1:String):Number
        {
            return Number(arg1.match(new RegExp("(\\d|\\.|\\,)", "g")).join("").split(",").join("."));
        }

        private function mouseMoveHandler(arg1:flash.events.MouseEvent):void
        {
            _active = true;
            return;
        }

		//unused functon, but maybe useful in future
        private function getColorFromGradient(arg1:Number):Number
        {
            var loc1:*=NaN;
            var loc2:*=NaN;
            var loc3:*=NaN;
            loc1 = arg1 * (tcolor >> 16) + (1 - arg1) * (tcolor2 >> 16);
            loc2 = arg1 * (tcolor >> 8) % 256 + (1 - arg1) * (tcolor2 >> 8) % 256;
            loc3 = arg1 * tcolor % 256 + (1 - arg1) * tcolor2 % 256;
            return loc1 << 16 | loc2 << 8 | loc3;
        }

        private function updateTags(event:flash.events.Event):void
        {
            var loc2:*=NaN;
            var loc3:*=NaN;
            var loc4:*=NaN;
            var loc5:*=NaN;
            var loc6:*=NaN;
            var loc7:*=NaN;
            var loc8:*=NaN;
            var scale:Number = 1;
            
            loc2 = 0;
            scale = 0;
            if (_active)
            {
                lasta = (-Math.min(Math.max(holder.mouseY, -250), 250)) / 150 * tspeed;
                lastb = Math.min(Math.max(holder.mouseX, -250), 250) / 150 * tspeed;
            }
            else 
            {
                lasta = lasta * 0.98;
                lastb = lastb * 0.98;
            }
            if (Math.abs(lasta) > 0.01 || Math.abs(lastb) > 0.01)
            {
                sineCosine(lasta, lastb, 0);
				var i:int = 0;
                while (i < _tagList.length) 
                {
                    loc2 = _tagList[i].cx;
                    loc3 = _tagList[i].cy * ca + _tagList[i].cz * (-sa);
                    loc4 = _tagList[i].cy * sa + _tagList[i].cz * ca;
                    loc5 = loc2 * cb + loc4 * sb;
                    loc6 = loc2 * (-sb) + loc4 * cb;
                    loc7 = loc5 * cc + loc3 * (-sc);
                    loc8 = loc5 * sc + loc3 * cc;
					
                    _tagList[i].cx = loc7;
                    _tagList[i].cy = loc8;
                    _tagList[i].cz = loc6;
					
                    scale = d / (d + loc6);
					
                    _tagList[i].x = loc7 * scale;
                    _tagList[i].y = loc8 * scale;
                    _tagList[i].scaleY = scale;
                    _tagList[i].scaleX = scale;
                    _tagList[i].alpha = scale / 2;
					
					//unvisible when tag is too small
					if ( _tagList[i].alpha < 0.5)
						_tagList[i].visible = false;
					else
						_tagList[i].visible = true;
					///////////////////////
					
                    i = (i + 1);
                }
                depthSort();
            }
            return;
        }

        private function resizeHolder():void
        {
            var scale:Number = 1;

            holder.x = this.stage.stageWidth / 2;
            holder.y = this.stage.stageHeight / 2;
            if (this.stage.stageWidth > this.stage.stageHeight)
            {
				scale = this.stage.stageHeight / 250;
            }
            else 
            {
				scale = this.stage.stageWidth / 250;
            }
            holder.scaleY = scale;
            holder.scaleX = scale;
			
			var size:int = Math.min(this.stage.stageWidth, this.stage.stageHeight);
			_image.width = size;
			_image.height = size;
			
			_image.x = this.stage.stageWidth / 2 - size / 2;
			_image.y = this.stage.stageHeight / 2 - size / 2;
			_image.alpha = 0.1;
			
            return;
        }

        private function mouseExitHandler(arg1:flash.events.Event):void
        {
            _active = false;
            return;
        }

        private function positionAll():void
        {
            var i:Number;
            var max:Number;
            var phi:Number;
            var theta:Number;

            var loc1:*;
            phi = NaN;
            theta = NaN;
            max = NaN;
            i = NaN;
            i = 0;
            max = _tagList.length;
            _tagList.sort(function ():*
            {
                return Math.random() < 0.5 ? 1 : -1;
            })
            trace(distr);
            while (i < max) 
            {
                if (distr)
                {
                    phi = Math.acos(-1 + 2 * i / max);
                    theta = Math.sqrt(max * Math.PI) * phi;
                }
                else 
                {
                    phi = Math.random() * Math.PI;
                    theta = Math.random() * 2 * Math.PI;
                }
                _tagList[i].cx = radius * Math.cos(theta) * Math.sin(phi);
                _tagList[i].cy = radius * Math.sin(theta) * Math.sin(phi);
                _tagList[i].cz = radius * Math.cos(phi);
				
                i = (i + 1);
				
            }
            return;
        }

        private function resizeHandler(arg1:flash.events.Event):void
        {
            resizeHolder();
            return;
        }

        private var _active:Boolean;

        private var hicolor:Number;

        private var originx:Number;

        private var originy:Number;

        private var sc:Number;

        private var _tagList:Array;

        private var sa:Number;

        private var cb:Number;

        private var d:Number;

        private var ca:Number;

        private var sb:Number;

        private var tspeed:Number;

        private var tcolor:Number;

        private var radius:Number;

        private var lasta:Number;

        private var holder:flash.display.MovieClip;

        private var distr:Boolean;

        private var tcolor2:Number;

        private var lastb:Number;

        private var cc:Number;

        private var myXML:XML;

        private var _sensitive:Number;

        private var myLoader:flash.net.URLLoader;
		
		private var _image:Bitmap;
    }
}


