package com.vanceinfo.meathill 
{
    import flash.display.*;
    import flash.events.*;
    import flash.filters.ColorMatrixFilter;
    import flash.geom.Matrix;
    import flash.net.*;
    import flash.text.*;
    
    import org.osmf.layout.AbsoluteLayoutFacet;
    
    public class Tag extends flash.display.Sprite
    {
        public function Tag(data:XML, textColor:Number, activeColor:Number)
        {
            var textFormat:TextFormat = new TextFormat();
            super();
            _data = data;
            _textColor = textColor;
			_activeColor = activeColor;
            _frameColor = _activeColor;
			
            _active = false;
			
			_label = new TextField();
            _label.autoSize = TextFieldAutoSize.LEFT;
            _label.selectable = false;
			
            textFormat.bold = true;
			textFormat.color = textColor;
			textFormat.font = "宋体";
			textFormat.size = Math.floor(Math.random() * 2) + 12;
            _label.defaultTextFormat = textFormat;
            _label.text = _data["@query"];
			_label.x = (-_label.width) / 2 + 3;
			_label.y = (-_label.height) / 2 ;

			_frame = new Sprite();
			
			
			_frame.graphics.beginFill(_frameColor, 0.2);
			
			var box:Matrix = new Matrix();
			box.createGradientBox(_label.textWidth + 5, _label.textHeight - 5, Math.PI / 2, 0, 10);
			
			_frame.graphics.beginGradientFill(GradientType.LINEAR, 
											[0xffffff, _frameColor], 
											[0, 0.8],
											[0, 255], 
											box,
											SpreadMethod.PAD,
											InterpolationMethod.LINEAR_RGB,
											0);
			//_frame.graphics.
			_frame.graphics.lineStyle(0, _frameColor, 0);
			_frame.graphics.drawRect(9, 10, _label.textWidth + 5, _label.textHeight -5);
			_frame.graphics.endFill();
			
			/*var m:Array = new Array();
			m = m.concat([1, 1, 1, 1, 1]);//red
			m = m.concat([0,0,0.5,0.5,0.5]);//green
			m = m.concat([0,0,0.5,0.5,0.5]);//blue
			m = m.concat([1,1,1,1,1]);//alpha
			_filter = new ColorMatrixFilter(m);*/
            this.addChild(_label);
			
            /*_word_bmpd = new BitmapData(_label.width, _label.height, true, 0);
            _word_bmpd.draw(_label, null, null, null, null, true);
            _word_bmp = new Bitmap(_word_bmpd, "auto", true);
            _word_bmp.x = (-_label.width) / 2 + 3;
            _word_bmp.y = (-_label.height) / 2 ;
            this.addChild(_word_bmp);*/
			
			this.addChild(_frame);
			
            _frame.x = (-_label.textWidth) / 2 - 10;
            _frame.y = (-_label.textHeight) / 2 - 2;
            _frame.visible = false;
			
            this.mouseChildren = false;
            this.buttonMode = true;
            this.addEventListener(MouseEvent.ROLL_OUT, mouseOutHandler);
            this.addEventListener(MouseEvent.ROLL_OVER, mouseOverHandler);
            this.addEventListener(MouseEvent.CLICK, mouseUpHandler);
			
            return;
        }

        private function mouseOverHandler(arg1:flash.events.MouseEvent):void
        {
            _frame.visible = true;
            _label.textColor = _activeColor;
			//_word_bmp.filters = [_filter];
			//this.addChild(_word_bmp);
			
            _active = true;
            return;
        }
		
		private function mouseOutHandler(arg1:flash.events.MouseEvent):void
		{
			_frame.visible = false;
			_label.textColor = _textColor;
			//_word_bmp.filters = [];
			//this.addChild(_word_bmp);
			_active = false;
			return;
		}
		
        public function set cy(arg1:Number):*
        {
            _cy = arg1;
            return;
        }

        public function get active():Boolean
        {
            return _active;
        }

        private function mouseUpHandler(arg1:flash.events.MouseEvent):void
        {
			URLNavigator.ChangePage(_data["@url"]);
            return;
        }

        public function get cx():Number
        {
            return _cx;
        }

        public function get cz():Number
        {
            return _cz;
        }

        public function get cy():Number
        {
            return _cy;
        }

        public function set cz(arg1:Number):*
        {
            _cz = arg1;
            return;
        }

        public function set cx(arg1:Number):*
        {
            _cx = arg1;
            return;
        }

        private function getNumberFromString(arg1:String):Number
        {
            return Number(arg1.match(new RegExp("(\\d|\\.|\\,)", "g")).join("").split(",").join("."));
        }

        private var _cx:Number;

        private var _cy:Number;

        private var _cz:Number;

        private var _label:TextField;

        private var _word_bmpd:flash.display.BitmapData;

        private var _active:Boolean;

        private var _word_bmp:flash.display.Bitmap;

        private var _textColor:Number;
        private var _frameColor:Number;
		private var _activeColor:Number;

        private var _frame:flash.display.Sprite;
		private var _filter:ColorMatrixFilter;

        private var _data:XML;
    }
}