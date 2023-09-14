// (A) INSTANT WORKER ACTIVATION
self.addEventListener("install", evt => self.skipWaiting());
 
// (B) CLAIM CONTROL INSTANTLY
self.addEventListener("activate", evt => self.clients.claim());
 
// (C) LISTEN TO PUSH
self.addEventListener("push", evt => {
  const data = evt.data.json();
  self.registration.showNotification(data.title, {
    body: data.body,
    //icon: data.icon,
    image: data.image
  });
});

self.addEventListener('notificationclick', function(event) {
    let url = 'https://elearning.pnj.ac.id/';
    event.notification.close(); // Android needs explicit close.
    event.waitUntil(
        clients.matchAll({type: 'window'}).then( windowClients => {
            // Check if there is already a window/tab open with the target URL
            for (var i = 0; i < windowClients.length; i++) {
                var client = windowClients[i];
                // If so, just focus it.
                if (client.url === url && 'focus' in client) {
                    return client.focus();
                }
            }
            // If not, then open the target URL in a new window/tab.
            if (clients.openWindow) {
                return clients.openWindow(url);
            }
        })
    );
});

/* PS. i just copy the notificationclick code from https://stackoverflow.com/questions/39418545/chrome-push-notification-how-to-open-url-adress-after-click */

