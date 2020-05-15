
const cacheName = 'Online Shopping';
const staticAssets = [
	'/',
	'/static/assets/css/style.css',
]

self.addEventListener('install', async e =>{
	const cache = await caches.open(cacheName);
	await cache.addAll(staticAssets);
	return self.skipWaiting();
});

self.addEventListener('activate', async e =>{
	self.clients.claim();
});

// self.addEventListener('fetch', async e =>{
// 	const req = e.request;
// 	const url = new URL(req.url);

// 	if (url.origin == location.origin) {
// 		e.respondWith(cacheFirst(req));
// 	}
// 	else{
// 		e.respondWith(networkkAndCache(req));
// 	}
// });

self.addEventListener('fetch', function(event) {
const promiseChain = doSomethingAsync()
      .then(() => doSomethingAsyncThatReturnsAURL(event))
      .then(someUrl => fetch(someUrl));
event.respondWith(promiseChain);
});


function askNotificationPermission() {
  // function to actually ask the permissions
  function handlePermission(permission) {
    // Whatever the user answers, we make sure Chrome stores the information
    if(!('permission' in Notification)) {
      Notification.permission = permission;
    }

    // set the button to shown or hidden, depending on what the user answers
    if(Notification.permission === 'denied' || Notification.permission === 'default') {
      notificationBtn.style.display = 'block';
    } else {
      notificationBtn.style.display = 'none';
    }
  }

  // Let's check if the browser supports notifications
  if (!('Notification' in window)) {
    console.log("This browser does not support notifications.");
  } else {
    if(checkNotificationPromise()) {
      Notification.requestPermission()
      .then((permission) => {
        handlePermission(permission);
      })
    } else {
      Notification.requestPermission(function(permission) {
        handlePermission(permission);
      });
    }
  }
}
// Notification.requestPermission()

var source = new EventSource('/events');

source.on('message', message => {
  var notification = new Notification(message.title, {
    body: message.body
  });
}); 