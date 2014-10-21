#!/usr/bin/env python2

from greshunkel.build import main
from greshunkel.context import BASE_CONTEXT, build_blog_context

if __name__ == '__main__':
    ctext = build_blog_context(BASE_CONTEXT)
    main(ctext)
