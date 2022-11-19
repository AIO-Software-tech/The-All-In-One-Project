using AIOLauncher;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Net;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Xml.Linq;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using static System.Windows.Forms.VisualStyles.VisualStyleElement;

namespace WindowsFormsApp1
{
    public partial class Form1 : Form
    {

        WebClient wc = new WebClient();

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

        //This is the home screen buttons
        private void Login_click(object sender, EventArgs e)
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

        private void AIOinGo_Click(object sender, EventArgs e)
        {
            Process.Start("AIOinGo.exe");
        }
        private void label4_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }


        //This is the apps tab buttons
        private void AIOInPython2_click(object sender, EventArgs e)
        {
            Process.Start("AIO.V-2.2.3.Rev-1-PY-version-3.7.py");
        }

        private void AIOinC2_Cick (object sender, EventArgs e)
        {
            Process.Start("AIOinC.exe");
        }

        private void AIOInGo2_click(object sender, EventArgs e)
        {
            Process.Start("AIOinGo.exe");
        }

        private void AIOinJS_click(object sender, EventArgs e)
        {
            Process.Start("AIOinJs.exe");
        }

        //This is the AIO In Other Langs
        private void AIOinFrench_Click(object sender, EventArgs e)
        {
            Process.Start("AIO In French.py");
        }

        //Misc
        private void label3_Click(object sender, EventArgs e)
        {

        }

        private void notifyIcon1_MouseDoubleClick(object sender, MouseEventArgs e)
        {
        
        }

        private void button9_Click(object sender, EventArgs e)
        {

        }


//Download Buttons
        private void DownloadButton1_click(object sender, EventArgs e)
        {
            wc.DownloadFileCompleted +=new AsyncCompletedEventHandler(FileCompleted);
            Uri aio224Url = new Uri("https://raw.githubusercontent.com/T0dCNg/The-All-In-One-Project/main/Old%20AIO/AIO%20v-2.2.4%20Rev-1%20PY-3.7.py");
            wc.DownloadFileAsync(aio224Url, "AIO-2.2.4.py");
        }

        private void FileCompleted(object sender, AsyncCompletedEventArgs e)
        {
            MessageBox.Show("Download Compleader\nFile Locaton: C:/Program Files (x86)/AIO Launcher/");
        }

        private void label9_Click(object sender, EventArgs e)
        {

        }

        private void button46_Click(object sender, EventArgs e)
        {

        }

        private void Home_Click(object sender, EventArgs e)
        {

        }

        private void label3_Click_1(object sender, EventArgs e)
        {

        }
    }
}
