//controls

module.exports = {
    welcome : function(req, res) {
        res.render('welcome', { 
            title: 'Tongshare Lite welcome!',
            RENREN_APP_URL: $RENREN_HOME_URL,
            APP_ID: $APP_ID});
    }
}
