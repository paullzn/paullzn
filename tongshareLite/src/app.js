
/**
 * Module dependencies.
 */

var express = require('express');

var app = module.exports = express.createServer();


// Configuration
require('./config')(app, express);

// Controllers
var controls = {
    _merge: function(obj) {
        for (key in obj) {
            this[key] = obj[key];
        }
    }
};

controls._merge(require('./controllers/controls'));
console.log(controls);

// Routes
require('./router')(app, express, controls);


app.listen(3000);
console.log("Express server listening on port %d in %s mode", app.address().port, app.settings.env);
