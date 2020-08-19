"""insert-releases

Revision ID: 765ed540939b
Revises: 8e9386e7a94b
Create Date: 2020-08-11 14:33:03.849692

"""
from alembic import op


# revision identifiers, used by Alembic.
revision = "765ed540939b"
down_revision = "8e9386e7a94b"
branch_labels = None
depends_on = None


def upgrade():
    releases = [
        {
            "codename": "warty",
            "version": "4.10",
            "name": "Warty Warthog",
            "development": False,
            "lts": False,
            "release_date": "2004-10-20",
            "esm_expires": "2004-10-20",
            "support_expires": "2004-10-20",
        },
        {
            "codename": "hoary",
            "version": "5.04",
            "name": "Hoary Hedgehog",
            "development": False,
            "lts": False,
            "release_date": "2005-04-08",
            "esm_expires": "2005-04-08",
            "support_expires": "2005-04-08",
        },
        {
            "codename": "breezy",
            "version": "5.10",
            "name": "Breezy Badger",
            "development": False,
            "lts": False,
            "release_date": "2005-10-13",
            "esm_expires": "2005-10-13",
            "support_expires": "2005-10-13",
        },
        {
            "codename": "dapper",
            "version": "6.06",
            "name": "Dapper Drake",
            "development": False,
            "lts": True,
            "release_date": "2006-06-01",
            "esm_expires": "2006-06-01",
            "support_expires": "2006-06-01",
        },
        {
            "codename": "edgy",
            "version": "6.10",
            "name": "Edgy Eft",
            "development": False,
            "lts": False,
            "release_date": "2006-10-26",
            "esm_expires": "2006-10-26",
            "support_expires": "2006-10-26",
        },
        {
            "codename": "feisty",
            "version": "7.04",
            "name": "Feisty Fawn",
            "development": False,
            "lts": False,
            "release_date": "2007-04-19",
            "esm_expires": "2007-04-19",
            "support_expires": "2007-04-19",
        },
        {
            "codename": "gutsy",
            "version": "7.10",
            "name": "Gutsy Gibbon",
            "development": False,
            "lts": False,
            "release_date": "2007-10-18",
            "esm_expires": "2007-10-18",
            "support_expires": "2007-10-18",
        },
        {
            "codename": "hardy",
            "version": "8.04",
            "name": "Hardy Heron",
            "development": False,
            "lts": True,
            "release_date": "2008-04-24",
            "esm_expires": "2008-04-24",
            "support_expires": "2008-04-24",
        },
        {
            "codename": "intrepid",
            "version": "8.10",
            "name": "Intrepid Ibex",
            "development": False,
            "lts": False,
            "release_date": "2008-10-30",
            "esm_expires": "2008-10-30",
            "support_expires": "2008-10-30",
        },
        {
            "codename": "jaunty",
            "version": "9.04",
            "name": "Jaunty Jackalope",
            "development": False,
            "lts": False,
            "release_date": "2009-04-23",
            "esm_expires": "2008-10-30",
            "support_expires": "2008-10-30",
        },
        {
            "codename": "karmic",
            "version": "9.10",
            "name": "Karmic Koala",
            "development": False,
            "lts": False,
            "release_date": "2009-10-29",
            "esm_expires": "2009-10-29",
            "support_expires": "2009-10-29",
        },
        {
            "codename": "lucid",
            "version": "10.04",
            "name": "Lucid Lynx",
            "development": False,
            "lts": True,
            "release_date": "2010-04-29",
            "esm_expires": "2010-04-29",
            "support_expires": "2010-04-29",
        },
        {
            "codename": "maverick",
            "version": "10.10",
            "name": "Maverick Meerkat",
            "development": False,
            "lts": False,
            "release_date": "2010-10-10",
            "esm_expires": "2010-10-10",
            "support_expires": "2010-10-10",
        },
        {
            "codename": "natty",
            "version": "11.04",
            "name": "Natty Narwhal",
            "development": False,
            "lts": False,
            "release_date": "2011-04-28",
            "esm_expires": "2011-04-28",
            "support_expires": "2011-04-28",
        },
        {
            "codename": "oneiric",
            "version": "11.10",
            "name": "Oneiric Ocelot",
            "development": False,
            "lts": False,
            "release_date": "2011-10-13",
            "esm_expires": "2011-10-13",
            "support_expires": "2011-10-13",
        },
        {
            "codename": "precise",
            "version": "12.04",
            "name": "Precise Pangolin",
            "development": False,
            "lts": True,
            "release_date": "2012-04-26",
            "esm_expires": "2021-04-30",
            "support_expires": "2012-04-26",
        },
        {
            "codename": "quantal",
            "version": "12.10",
            "name": "Quantal Quetzal",
            "development": False,
            "lts": False,
            "release_date": "2012-10-18",
            "esm_expires": "2012-10-18",
            "support_expires": "2012-10-18",
        },
        {
            "codename": "raring",
            "version": "13.04",
            "name": "Raring Ringtail",
            "development": False,
            "lts": False,
            "release_date": "2013-04-25",
            "esm_expires": "2013-04-25",
            "support_expires": "2013-04-25",
        },
        {
            "codename": "saucy",
            "version": "13.10",
            "name": "Saucy Salamander",
            "development": False,
            "lts": False,
            "release_date": "2013-10-17",
            "esm_expires": "2013-10-17",
            "support_expires": "2013-10-17",
        },
        {
            "codename": "trusty",
            "version": "14.04",
            "name": "Trusty Tahr",
            "development": False,
            "lts": True,
            "release_date": "2014-04-17",
            "esm_expires": "2022-04-30",
            "support_expires": "2019-04-30",
        },
        {
            "codename": "utopic",
            "version": "14.10",
            "name": "Utopic Unicorn",
            "development": False,
            "lts": False,
            "release_date": "2014-10-23",
            "esm_expires": "2014-10-23",
            "support_expires": "2014-10-23",
        },
        {
            "codename": "vivid",
            "version": "15.04",
            "name": "Vivid Vervet",
            "development": False,
            "lts": False,
            "release_date": "2015-04-23",
            "esm_expires": "2015-04-23",
            "support_expires": "2015-04-23",
        },
        {
            "codename": "wily",
            "version": "15.10",
            "name": "Wily Werewolf",
            "development": False,
            "lts": False,
            "release_date": "2015-10-22",
            "esm_expires": "2015-10-22",
            "support_expires": "2015-10-22",
        },
        {
            "codename": "xenial",
            "version": "16.04",
            "name": "Xenial Xerus",
            "development": False,
            "lts": True,
            "release_date": "2016-04-21",
            "esm_expires": "2024-04-30",
            "support_expires": "2021-04-30",
        },
        {
            "codename": "yakkety",
            "version": "16.10",
            "name": "Yakkety Yak",
            "development": False,
            "lts": False,
            "release_date": "2016-10-13",
            "esm_expires": "2016-10-13",
            "support_expires": "2016-10-13",
        },
        {
            "codename": "zesty",
            "version": "17.04",
            "name": "Zesty Zapus",
            "development": False,
            "lts": False,
            "release_date": "2017-04-13",
            "esm_expires": "2017-04-13",
            "support_expires": "2017-04-13",
        },
        {
            "codename": "artful",
            "version": "17.10",
            "name": "Artful Aardvark",
            "development": False,
            "lts": False,
            "release_date": "2017-10-19",
            "esm_expires": "2017-10-19",
            "support_expires": "2017-10-19",
        },
        {
            "codename": "bionic",
            "version": "18.04",
            "name": "Bionic Beaver",
            "development": False,
            "lts": True,
            "release_date": "2018-04-26",
            "esm_expires": "2028-04-30",
            "support_expires": "2023-04-30",
        },
        {
            "codename": "cosmic",
            "version": "18.10",
            "name": "Cosmic Cuttlefish",
            "development": False,
            "lts": False,
            "release_date": "2018-10-18",
            "esm_expires": "2018-10-18",
            "support_expires": "2018-10-18",
        },
        {
            "codename": "disco",
            "version": "19.04",
            "name": "Disco Dingo",
            "development": False,
            "lts": False,
            "release_date": "2019-04-18",
            "esm_expires": "2019-04-18",
            "support_expires": "2019-04-18",
        },
        {
            "codename": "eoan",
            "version": "19.10",
            "name": "Eoan Ermine",
            "development": False,
            "lts": False,
            "release_date": "2019-10-17",
            "esm_expires": "2020-07-31",
            "support_expires": "2019-10-17",
        },
        {
            "codename": "focal",
            "version": "20.04",
            "name": "Focal Fossa",
            "development": False,
            "lts": True,
            "release_date": "2020-04-23",
            "esm_expires": "2030-04-30",
            "support_expires": "2025-04-30",
        },
        {
            "codename": "groovy",
            "version": "20.10",
            "name": "Groovy Gorilla",
            "development": True,
            "lts": False,
            "release_date": "2020-10-20",
            "esm_expires": "2021-07-31",
            "support_expires": "2021-07-31",
        },
        {"codename": "upstream", "name": "Upstream"},
    ]

    for release in releases:
        release_fields = ",".join(str(k) for k, v in release.items())
        release_values = ",".join(f"'{v}'" for v in release.values())

        op.execute(
            f"INSERT INTO release ({release_fields}) "
            f"VALUES ({release_values}) "
            f"ON CONFLICT DO NOTHING"
        )


def downgrade():
    op.execute("TRUNCATE TABLE release")