if __name__ == "__main__":
    import sys, os
    #sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), '../../'))
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
    from blogsley_flask.app import create_app
    app = create_app()

from __blogsley__ import db
from blogsley_flask.models.users import User
from blogsley_flask.models.blog import Post

block = """
{
  "type": "Page",
  "id": "UcGgZlHKqLcUtZrhD1gmc",
  "_value": null,
  "html": "",
  "children": [
    {
      "type": "Title",
      "id": "7D51SWIHpZ_8jyAxtKFIr",
      "_value": "Bazinga!",
      "html": "<h1>Bazinga!</h1>",
      "children": []
    },
    {
      "type": "Paragraph",
      "id": "gA1RyeFDpcEEAfBdXhQvU",
      "_value": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
      "html": "<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>",
      "children": [],
      "content": {
        "type": "doc",
        "content": [
          {
            "type": "paragraph",
            "content": [
              {
                "type": "text",
                "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
              }
            ]
          }
        ]
      }
    },
    {
      "type": "Image",
      "id": "U1AJAk6v8pOqcchxSAZOH",
      "_value": null,
      "html": "",
      "children": [],
      "src": "statics/images/journal-on-desk.jpg",
      "width": 256,
      "height": 256
    },
    {
      "type": "Heading",
      "id": "2wWjwHazm8jVLLZAHnbvl",
      "_value": "Heading",
      "html": "<h2>Heading</h2>",
      "children": [],
      "content": {
        "type": "doc",
        "content": [
          {
            "type": "heading",
            "attrs": {
              "level": 2
            },
            "content": [
              {
                "type": "text",
                "text": "Heading"
              }
            ]
          }
        ]
      }
    },
    {
      "type": "Paragraph",
      "id": "BXVQVXVk5KJCh48gEubqp",
      "_value": "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
      "html": "<p>Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>",
      "children": [],
      "content": {
        "type": "doc",
        "content": [
          {
            "type": "paragraph",
            "content": [
              {
                "type": "text",
                "text": "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
              }
            ]
          }
        ]
      }
    },
    {
      "type": "Html",
      "id": "tTaKSi7UPbuywEajPrcZY",
      "_value": null,
      "html": "<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p><p>Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>",
      "children": [],
      "content": {
        "type": "doc",
        "content": [
          {
            "type": "paragraph",
            "content": [
              {
                "type": "text",
                "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
              }
            ]
          },
          {
            "type": "paragraph",
            "content": [
              {
                "type": "text",
                "text": "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
              }
            ]
          }
        ]
      }
    },
    {
      "type": "List",
      "id": "N6_UoyNfcEr24e581nsUP",
      "_value": [
        "Get Milk",
        "Get Bread",
        "Get Butter"
      ],
      "html": "<ul><li><p>Get Milk</p></li><li><p>Get Bread</p></li><li><p>Get Butter</p></li></ul>",
      "children": [],
      "content": {
        "type": "doc",
        "content": [
          {
            "type": "bullet_list",
            "content": [
              {
                "type": "list_item",
                "content": [
                  {
                    "type": "paragraph",
                    "content": [
                      {
                        "type": "text",
                        "text": "Get Milk"
                      }
                    ]
                  }
                ]
              },
              {
                "type": "list_item",
                "content": [
                  {
                    "type": "paragraph",
                    "content": [
                      {
                        "type": "text",
                        "text": "Get Bread"
                      }
                    ]
                  }
                ]
              },
              {
                "type": "list_item",
                "content": [
                  {
                    "type": "paragraph",
                    "content": [
                      {
                        "type": "text",
                        "text": "Get Butter"
                      }
                    ]
                  }
                ]
              }
            ]
          }
        ]
      }
    }
  ]
}
"""


def populate():
    u = User(
        username="admin",
        first_name="The",
        last_name="Admin",
        email="admin@example.com",
        role="Admin",
        about_me="I am the Admin",
    )
    u.set_password("admin")
    db.session.add(u)
    db.session.commit()

    u = User(
        username="john",
        first_name="John",
        last_name="Doe",
        email="john@example.com",
        role="Editor",
        about_me="I am an Editor",
    )
    u.set_password("x")
    db.session.add(u)
    db.session.commit()

    p = Post(
        title="Blogsley, Web Publishing Evolved",
        block=block,
        body="Blogsley is a CMS for the JAMstack",
        author=u,
    )
    db.session.add(p)
    db.session.commit()

    u = User(
        username="susan",
        first_name="Susan",
        last_name="Smith",
        email="susan@example.com",
        role="Author",
        about_me="I am an Author",
    )
    u.set_password("x")
    db.session.add(u)
    db.session.commit()

    p = Post(
        title="Python is cool!",
        block=block,
        body="I love writing programs in Python",
        author=u,
    )
    db.session.add(p)
    db.session.commit()

    u = User(
        username="joe",
        first_name="Joe",
        last_name="Jackson",
        email="joe@example.com",
        role="Reader",
        about_me="I am a Reader",
    )
    u.set_password("x")
    db.session.add(u)
    db.session.commit()

    users = User.query.all()
    print(users)

    posts = Post.query.all()
    for p in posts:
        print(p.id, p.author.username, p.body)


if __name__ == "__main__":
    populate()

