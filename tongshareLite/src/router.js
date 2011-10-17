//route config for app

module.exports = function(app, express, controls) {
  app.get('/tongshare/?', function(req, res){
    res.render('index', {
      title: 'Tongshare Lite'
    });
  });

  app.get('/welcome/?', controls.welcome);
  
}
