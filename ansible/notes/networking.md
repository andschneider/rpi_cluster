# Networking

For the nodes to be able to reach the internet, a NAT needs to be setup on the master node. This will allow forwarding from the `wlan0` to `eht0`.

```bash
iptables -t nat -A POSTROUTING -o wlan0 -j MASQUERADE
iptables -A FORWARD -i wlan0 -o eht0 -m state \
  --state RELATED,ESTABLISHED -j ACCEPT
iptables -A FORWARD -i eth0 -o wlan0 ACCEPT
```
