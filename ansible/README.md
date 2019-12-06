# Ansible configurations

## Initial set up

Installs:

- Docker 19.03
- Kubernetes 1.16.3

Run playbook:

```bash
ansible-playbook --private-key=~/.ssh/rpi5 -i ./hosts init_config.yml -v
```
