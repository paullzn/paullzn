//controls
var http = require('http')

module.exports = function (libs) {

    helpers = function(libs) {
    var API_HOST = 'http://api.renren.com/resetserver.do';
    
    function _makeRApiRequest(param, receiver, callback,  options) {
        var client = http.createClient(80, "www.renren.com");
        
        return _getSignature(param)

        var headers = {
            'Host': 'www.renren.com',
            'Content-Type': '',
            'Content-Length': data.length
        }
        
        var request = client.request('POST', path, headers)

        request.on('response', _onRApiResponse);
        request.send(data);
        request.end();
    }

    function _getSignature(param) {
        var list = [];
        for (key in param) {
            list.push(key + '=' + param[key]);
        } 
        list.sort();
        var str = list.join('') + $API_SECRET;
        return libs.md5.hex_md5(str) 
    }

    function _onRApiResponse(response) {
        response.on('data', function(chunk) {
        
        
        
        }); 
        response.end('')
    }


    return {
        makeRApiRequest: _makeRApiRequest
    };
    }(libs);
};
