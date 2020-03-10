#!/bin/bash
gunicorn easy_seo:app --daemon
python worker.py