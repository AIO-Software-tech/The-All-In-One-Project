using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.Drawing;
using System.Linq;
using System.Net;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Xml.Linq;

namespace WindowsFormsApp1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void label5_Click(object sender, EventArgs e)
        {

        }

        private void AIOinPython_Click(object sender, EventArgs e)
        {
            Process.Start("AIO.V-2.2.3.Rev-1-PY-version-3.7.py");
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Process.Start("AIOinC.exe");
        }

        private void AIOInPython2_click(object sender, EventArgs e)
        {
            Process.Start("AIO.V-2.2.3.Rev-1-PY-version-3.7.py");
        }

        private void label3_Click(object sender, EventArgs e)
        {

        }

        private void notifyIcon1_MouseDoubleClick(object sender, MouseEventArgs e)
        {
            using (var client = new WebClient())
                client.DownloadFile("", "a.mpeg");
        }
    }
}
