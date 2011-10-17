//configuration for both dev and prod env
module.exports = function(app, express) {
  app.configure(function(){
    app.set('views', __dirname + '/views');
    app.set('view engine', 'jade');
    app.use(express.bodyParser());
    app.use(express.methodOverride());
    app.use(app.router);
    app.use(express.static(__dirname + '/public'));
  });

  require('./configs/dev.js')(app, express);
  require('./configs/prod.js')(app, express);

  $APP_ID = "159214";
  $API_KEY = "4c085892afce48e5b4f60cf071b470cc";
  $API_SECRET = "07bda69d16b64adda22571baa37442ab";
  $RENREN_HOME_URL = "http://apps.renren.com/tongshare";
}
