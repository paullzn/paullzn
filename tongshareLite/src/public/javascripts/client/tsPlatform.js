//Copyright Zhaonan Li 2011
//base interface for creating object to html

var DEBUG_MODE = true;

function LOG(msg) {
    if (DEBUG_MODE === true)
        console.log(msg);
}

$ts.Platform = (function() {
    var __eventCallback,
        __eventReceiver,
        _flushDataTimer,
        _persistDict,
        _persisDictChanged,
        _lastKeyDown;
    
    __eventCallback = null;
    __eventReceiver = null;
    
    function _attachEventHandlers(receiver, callback) {
        __eventCallback = callback;
        __eventReceiver = receiver;
    }

    function _createTimer(interval, receiver, callback) {
        var timerObject = {
            handle: -1,
            receiver: receiver,
            callback: callback,
            interval: interval
        };

        timerObject.start = function() {
            timerObj.stop();
            timerObj.handle = setInterval(
                function() { timerObj.callback.call(timerObj.receiver); },
                timerObj.interval
            );
        };

        timerObj.stop = function() {
            if (timerObj.handle !== -1) {
                clearInterval(timerObj.handle);
                timerObj.handle = -1;
            }
        }

        timerObj.setCallback = function(newReceiver, newCallback) {
            timerObj.receiver = newReceiver;
            timerObj.callback = newCallback;

            if (timerObj.handle !== -1) {
                timerObj.stop();
                timerObj.start();
            }
        }
    
        timerObj.setInterval = function(newInterval) {
            timerObj.interval = newInterval;

            if (timerObj.handle !== -1) {
                timerObj.stop();
                timerObj.start();
            }
        }

        timerObj.destroy = function() {
            timerObj.stop();
            timerObj.receiver = null;
            timerObj.callback = null;
        }
        
        timerObj.running = function() {
            return timerObk.handle !== -1;
        }
        return timerObj;
    }

    function _keydownHandler(keyCode) {
        var times = 1;
        if (_lastKeyDown && _lastKeyDown.keyCode === keyCode) {
            times = _lastKeyDown.times + 1;

            if (times === 2) {
                _keypressHandler({
                    keyCode: keyCode,
                    isDown: true,
                    isHold: true
                });
            }
        }

        var eventData = {
            keyCode: keyCode,
            isDown: true,
            isHold: true,
            times: times
        };

        _keypressHandler(eventData);
        _lastKeydown = eventData;
    }

    function _keyupHandler(keyCode) {
        var eventData = {
            keyCode: keyCode,
            isDown: false,
            isHold: (_lastKeyDown && _lastKeyDown.times > 1)
        };
        _keypressHandler(eventData);
        _lastKeyDown = null;
    }

    function _keypressHandler(eventData) {
        var action = null; 
    }

    function _loadURL(url, receiver, callback,  options) {
        var xhr = new XMLHttpRequest();
        xhr.url = url;
        xhr.onreadystatechange = function() {
            _loadURLHandler(req);
        }
        if (options) { 
            xhr.method = options.method;
        }
        if (xhr.method !== "POST") { 
            xhr.method = "GET";
        }
        options.receiver = receiver;
        options.callback = callback;
        options.url = url;
        xhr.options = options;
        if (options.content_type) {
            xhr.setRequestHeader("Content-type", options.content_type);
        }
        if (options.compress) {
            xhr.setRequestHeader("X-Compress", "gzip");
        }
        if (!options.data) {
            options.data = "";
        }
        if (options.method === "GET") {
            xhr.send();
        } else {
            xhr.setRequestHeader("Content-length", options.data.length);
            xhr.send(options.data);
        }
        LOG("loadURL : " + url + " data= " + options.data);
    }

    function _loadURLHandler(req) {
        if (xhr.readyState === 4) {
            if (xhr.status === 200) {
                if (xhr.options.xmlparse) {
                    xhr.options.callback.call(xhr.options.receiver, $ts.Platform.XML.parseToXML(xhr.responseText), xhr.options);
                }else {
                    xhr.options.callback.call(rep.options.receiver, xhr.responseText, xhr.options);
                } 
            } else {
                LOG("URL request failed: status:" + xhr.status + " url:" + xhr.url + " method:" + xhr.method);
                if (xhr.options.errorCallback) {
                    xhr.errorCallback.call(xhr.receiver, xhr.status, {
                        errorMsg: xhr.statusText,
                        data: xhr.responseText
                    });
                }else {
                    LOG("Nobody handle this loadURL error!!"); 
                }
            }
        }  
    }

    return {
        attachEventHandlers: _attachEventHandlers,
        createTimer: _createTimer,
        keydownHandler: _keydownHandler,
        keypressHandler: _keypressHandler,
        keyupHandler: _keyupHandler,
        loadURL: _loadURL,
        properties : {
            platform: "web"    
        } 
    }
})();
